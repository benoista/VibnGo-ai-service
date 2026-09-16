# AI Service

FastAPI service that exposes a chat endpoint backed by [Ollama](https://ollama.com).

## Requirements

- Python 3.11+
- [Ollama](https://ollama.com) (running natively for dev, or containerized for prod)
- Docker & Docker Compose (optional, for containerized runs)

## Setup

1. Copy the environment file and adjust as needed:

   ```bash
   cp .env.example .env
   ```

2. Install dependencies — **only needed if you run the service locally without Docker**. When running via `docker compose`, the `Dockerfile` installs them at build time, so this step can be skipped:

   ```bash
   pip install -r requirements.txt
   ```

## Environment variables

| Variable       | Description                                                                 |
| -------------- | ---------------------------------------------------------------------------- |
| `OLLAMA_HOST`  | URL of the Ollama server (e.g. `http://host.docker.internal:11434` in dev). |
| `OLLAMA_MODEL` | Model name to use for generation (e.g. `mistral`).                          |

## Running

### Locally

```bash
uvicorn main:app --reload
```

### With Docker Compose

Dev (Ollama running natively on the host):

```bash
docker compose up
```

Prod (Ollama containerized alongside the service):

```bash
docker compose --profile prod up
```

The service is available at `http://localhost:8000`.

## API

### `GET /health`

Health check.

```json
{ "status": "ok" }
```

### `POST /chat`

Forwards a prompt to Ollama and returns its response.

Request body:

```json
{ "prompt": "Hello, how are you?" }
```

## Contributing

1. Create a branch from `main` for your change.
2. Keep changes scoped to the AI service (`apps/ai-service`).
3. Make sure the service starts and `/health` and `/chat` work locally before opening a PR:

   ```bash
   uvicorn main:app --reload
   curl http://localhost:8000/health
   ```

4. Update `.env.example` and this README if you add or change environment variables or endpoints.
5. Open a pull request with a clear description of the change and how it was tested.
