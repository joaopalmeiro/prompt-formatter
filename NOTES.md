# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- Google/Gemini:
  - https://ai.google.dev/gemini-api/docs/llms.txt
- https://llmstxt.site/
- https://directory.llmstxt.cloud/
- https://ai.google.dev/gemini-api/docs/caching?lang=python
  - https://ai.google.dev/gemini-api/docs/caching?lang=python#caching-using-openai
- https://llmstxt.org/domains.html

## Commands

```bash
deactivate && uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```
