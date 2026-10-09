# Contributing

## Development setup

1. Install a current Node.js LTS release and Python 3.10 or newer.
2. From this directory, run `npm install`.
3. Create a Python virtual environment and install `requirements.txt` if OCR
   support is needed.
4. Copy `.env.example` to `.env` and adjust local settings.

## Making changes

- Keep document evidence and generated conclusions clearly separated.
- Keep calculations deterministic and in JavaScript rather than delegating
  arithmetic to a language model.
- Do not commit documents, model weights, local databases, `.env` files, or
  generated reports.
- Add or update focused tests for behavior changes.

Before opening a pull request, run:

```powershell
npm run lint
npm test
npm run build
```

Describe environment-dependent checks, such as Ollama, GPU, or OCR checks,
separately from checks that run without external services.
