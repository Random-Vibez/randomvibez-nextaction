# Security and privacy notes

- NextAction is static and browser-local. There is no backend, network request, account, analytics, reminder, or portal integration.
- The app stores only a bounded, allowlisted schema in `localStorage`, with version and item-count/size limits.
- JSON import validates the complete candidate before replacing existing state (atomic validation). Exports and printouts are unencrypted.
- User text is rendered with `textContent`; user links must be HTTPS and open with `noopener noreferrer`.
- Do not store passwords, authentication codes, confidential attachments, government identifiers, or other secrets.
- The included `.htaccess` is defense in depth for Apache deployments; verify equivalent headers in the actual server configuration.

Report suspected issues to the project maintainer rather than including personal application data.
