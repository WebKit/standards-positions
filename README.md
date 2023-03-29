# WebKit's positions on emerging web specifications

## What is this Repository?

The [WebKit Open Source Project](https://webkit.org/) uses [this GitHub repository](https://github.com/WebKit/standards-positions) to come to consensus on various web specification proposals. We do this through [issues in this repository](https://github.com/WebKit/standards-positions/issues/).

Please [file an issue](https://github.com/WebKit/standards-positions/issues/new) if you'd like us to generate a position on some web-facing API.

For a browsable list of settled positions, see [all closed issues with a position label](https://github.com/WebKit/standards-positions/issues?q=is:issue+is:closed+label%3A%22position%3A+support%22%2C%22position%3A+neutral%22%2C%22position%3A+oppose%22%2C%22position%3A+under+consideration%22%2C%22position%3A+not+considering%22). For positions that pre-date this repository, see the [webkit-dev mailing list archives](https://lists.webkit.org/pipermail/webkit-dev/).

### Possible positions

Only once a label is assigned to an issue does it represent WebKit's position.
Individual responses to issues do not represent WebKit's position on a specification or feature thereof.
Positions are not final. We are happy to revisit positions as new information becomes available.

- `support` - WebKit sees this specification as conceptually good, and worth prototyping, getting feedback on its value, and iterating.
- `neutral` - WebKit does not see this specification as harmful, but is not convinced that it is a good approach or worth working on.
- `oppose` - WebKit considers this specification to be harmful in its current state.
- `not considering` - WebKit does not intend to look at this specification in the near future.

Note that positions on this repository do not reflect implementation status. We might like something we do not get around to implement for one reason or another. And we might dislike something we nevertheless have to implement.

#### Other possible issue states

- `blocked` - Coming to a position is blocked on issues identified with the spec or proposal.
- `duplicate` - The issue is a duplicate of another issue.
- `invalid` - The issue is not about a specification which would be implemented in a browser engine such as WebKit.

### Resolving an issue with a position

Reviewing proposals is always encouraged and as such please leave feedback and add relevant labels to issues.

To add a "position: _X_" label where _X_ is one of the positions documented above, please follow this simple process so there is opportunity for WebKit-at-large to reflect and chime in as needed. As WebKit consists of many individuals across companies and timezones some asynchronicity is desirable.

1. Leave a comment with your suggested "position: _X_" label, rationale (as needed), and a deadline for further feedback that’s at least 7 days in the future. Depending on the time of year or complexity of the item under review you might want to prolong this.
2. After the deadline has passed, if there were no requests for more time, no objections, and ideally you had some support through thumbs up or comments with additional context, your suggested "position: _X_" label can be added.
3. You did it! 🎉

## Helpful links for triaging standards position requests

- [Open issues not tracked in the backlog project](https://github.com/WebKit/standards-positions/issues?q=is%3Aopen+is%3Aissue+-project%3Awebkit%2F1+)
- [Open issues without a position label](https://github.com/WebKit/standards-positions/issues?q=is%3Aopen+is%3Aissue+-label%3A%22position%3A+neutral%22+-label%3A%22position%3A+not+considering%22+-label%3A%22position%3A+oppose%22+-label%3A%22position%3A+support%22+-label%3A%22position%3A+under+consideration%22+-label%3Ameta)
- [Open issues with a position label](https://github.com/WebKit/standards-positions/issues?q=is%3Aopen+is%3Aissue+label%3A%22position%3A+neutral%22%2C%22position%3A+not+considering%22%2C%22position%3A+oppose%22%2C%22position%3A+support%22%2C%22position%3A+under+consideration%22)
