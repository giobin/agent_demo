# agent_demo

Repo di demo per sperimentare agenti AI in Python.

Contiene esempi su:

- agenti con `smolagents`
- tool calling e Model Context Protocol con un server MCP locale
- memoria persistente con `mem0`, Qdrant in-memory e Hugging Face

## Requisiti

- Python 3.10+
- `uv`
- un token Hugging Face per i notebook che chiamano modelli hosted

Se non hai `uv`, installalo seguendo la guida ufficiale: https://docs.astral.sh/uv/getting-started/installation/

## Setup

Clona il repo e installa le dipendenze:

```bash
git clone https://github.com/giobin/agent_demo.git
cd agent_demo
uv sync
```

`uv sync` crea o aggiorna l'ambiente virtuale locale `.venv` usando `pyproject.toml` e `uv.lock`.

## Variabili d'ambiente

Copia il file di esempio:

```bash
cp .env.example .env
```

Poi inserisci il tuo token Hugging Face:

```bash
HF_TOKEN=hf_il_tuo_token
```

Puoi creare un token da https://hf.co/settings/tokens.