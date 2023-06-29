#!/usr/bin/env python

import argparse, json, os, requests


# Utilities
def write_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2, separators=(",", ": "))
        f.write("\n")


# General processing
def process(issues):
    summary = []
    for issue in issues:
        if is_ignorable_issue(issue):
            continue

        summary_item = {"id": issue["html_url"]}
        summary_item.update(process_labels(issue["labels"]))
        summary_item.update(process_body(issue))

        summary.append(summary_item)
    write_json("summary.json", summary)


def is_ignorable_issue(issue):
    if "pull_request" in issue:
        return True
    for label in issue["labels"]:
        if label["name"] in ("duplicate", "invalid", "meta", "proposal withdrawn"):
            return True
    return False


def process_labels(labels):
    position = None
    venues = []
    concerns = []
    topics = []

    for label in labels:
        # Position
        if label["name"] == "blocked":
            assert position is None
            position = "blocked"
        elif label["name"].startswith("position: "):
            assert position is None
            position = label["name"][len("position: ") :]
        # Venue
        elif label["name"] == "venue: AOM":
            venues.append("AOM")
        elif label["name"] == "venue: Ecma TC39":
            venues.append("TC39")
        elif label["name"].startswith("venue: IETF"):
            venues.append("IETF")
        elif label["name"].startswith("venue: WHATWG"):
            venues.append("WHATWG")
        elif label["name"].startswith("venue: W3C"):
            venues.append("W3C")
        elif label["name"].startswith("venue: "):
            venues.append("Other")
        # Concerns
        elif label["name"].startswith("concerns: "):
            concerns.append(label["name"][len("concerns: ") :])
        # Topics
        elif label["name"].startswith("topic: "):
            topics.append(label["name"][len("topic: ") :])

    return {
        "position": position,
        "venues": list(dict.fromkeys(venues)),
        "concerns": concerns,
        "topics": topics,
    }


def process_body(issue):
    lines = issue["body"].splitlines()

    body = {
        "title": None,
        "url": None,
        "github": None,
        "issues": None,
        "explainer": None,
        "tag": None,
        "mozilla": None,
        "bugzilla": None,
        "radar": None,
    }

    legacy_mapping = {
        "Spec Title": "title",
        "Title": "title",
        "Spec URL": "url",
        "URL": "url",
        "GitHub repository": "github",
        "Issue Tracker (if not the repository's issue tracker)": "issues",
        "Explainer (if not README.md in the repository)": "explainer",
        "TAG Design Review": "tag",
        "Mozilla standards-positions issue": "mozilla",
        "WebKit Bugzilla": "bugzilla",
        "Radar": "radar",
    }

    yaml_mapping = {
        "Title of the spec": "title",
        "URL to the spec": "url",
        "URL to the spec's repository": "github",
        "Issue Tracker URL": "issues",
        "Explainer URL": "explainer",
        "TAG Design Review URL": "tag",
        "Mozilla standards-positions issue URL": "mozilla",
        "WebKit Bugzilla URL": "bugzilla",
        "Radar URL": "radar",
    }

    # Legacy mapping applies until the YAML change
    if issue["number"] < 162:
        for line in lines:
            for prefix, key in legacy_mapping.items():
                text_prefix = f"* {prefix}: "
                if line.startswith(text_prefix):
                    assert body[key] is None
                    value = line[len(text_prefix) :].strip()
                    if value:
                        body[key] = value
    else:
        expect_response = None
        skip = False
        for line in lines:
            if line == "### Description":
                break
            for title, key in yaml_mapping.items():
                text_title = f"### {title}"
                if line == text_title:
                    expect_response = key
                    skip = True
                    break
            if skip:
                skip = False
                continue
            if expect_response:
                value = line.strip()
                if value and value != "_No response_":
                    body[expect_response] = value
                    expect_response = None
    return body


# Setup
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="get the latest issue data from GitHub",
    )
    parser.add_argument("-p", "--process", action="store_true", help="process the data")
    args = parser.parse_args()

    if args.update:
        # GitHub allows us to read issues in increments of 100, called pages. As we don't have more
        # than 3 pages we're not optimizing this for now.
        data = []
        page = 1
        while True:
            try:
                response = requests.get(
                    f"https://api.github.com/repos/WebKit/standards-positions/issues?direction=asc&state=all&per_page=100&page={page}",
                    timeout=5,
                )
                response.raise_for_status()
            except Exception:
                print("Updated failed, network failure or request timed out.")
                exit(1)
            temp_data = response.json()
            if not temp_data:
                break
            data.extend(temp_data)
            page += 1
        write_json("summary-data.json", data)
        print("Done, thanks for updating!")
        exit(0)

    if args.process:
        if not os.path.exists("summary-data.json"):
            print("Sorry, you have to update first.")
            exit(1)

        with open("summary-data.json", "rb") as f:
            data = json.load(f)
        process(data)


if __name__ == "__main__":
    main()
