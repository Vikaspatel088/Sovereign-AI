# Security

## Scope and security model

Sovereign AI Workbench is designed for local operation. The API binds to the
local machine by default and the UI uses a local API origin. This is not a
security certification or a guarantee that a host is air-gapped.

Uploaded files are processed temporarily by the API. Do not use this project
with documents that you are not authorized to process. Keep Ollama, the API,
and the development server on trusted interfaces and do not expose them to a
network without adding authentication and a deployment-specific threat model.

## Repository hygiene

Real environment files, uploaded documents, generated reports, databases,
model weights, and caches are excluded by `.gitignore`. Never put credentials
or private documents in an issue, pull request, log, or commit.

## Dependency review

Run `npm audit` before a release. The current dependency tree includes known
advisories in `xlsx` and transitive packages; these should be reviewed before
using the system beyond local development.

## Reporting a vulnerability

Please do not disclose exploitable details in a public issue. Contact the
maintainer through the private security reporting features on the
[GitHub profile](https://github.com/Vikaspatel088), including reproduction
steps, affected versions, and a suggested mitigation.
