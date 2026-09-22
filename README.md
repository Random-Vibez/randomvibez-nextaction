# NextAction

A browser-local follow-up board for job, internship, grant, and school applications. It keeps the next concrete action visible without an account, backend, reminder service, or connection to application portals.

## Use
Open `index.html` or serve this folder with any static HTTP server. Add an application, edit or delete it, print the board, or export a bounded JSON backup. Imports are accepted only when the complete versioned schema passes validation; failed imports leave the current board untouched.

## Privacy boundary
Records and the one first-party acceptance preference use `localStorage`. Nothing is uploaded or fetched at runtime. Do not enter passwords, confidential materials, or unnecessary sensitive identifiers. JSON exports and printouts are unencrypted. The source-link field is displayed as a user-provided HTTPS link and is never checked or fetched.

## Limits
Maximum 80 records, 50,000-character stored state, and 100,000-byte import file. Schema version is `nextaction:v1`.

## Verification
Run `python3 tests/test_static.py` and `node --check app.js` from this directory. A local preview can be served with `python3 -m http.server 8765`.
