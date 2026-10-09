# Development

## Local commands

Run commands from the `WEB` directory:

```powershell
npm install
npm run lint
npm test
npm run build
```

Start the API and UI in separate PowerShell windows:

```powershell
npm run server
npm run dev
```

The API listens on `http://127.0.0.1:8787` and Vite serves the UI at
`http://127.0.0.1:5173` by default.

## Optional local services

Install Ollama separately, run `ollama serve`, and pull the configured models.
The API reports model availability through `/health`; tests do not download
models or require a GPU. Install RapidOCR in a Python virtual environment for
PNG/JPG OCR:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Testing expectations

The automated suite covers deterministic calculations, verification guards,
retrieval, demo evidence, and the health endpoint. Tests are intentionally
independent of Ollama, GPU hardware, model weights, and private documents.
Those integrations require separate environment-dependent validation.
