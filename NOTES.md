# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- Google/Gemini:
  - https://ai.google.dev/gemini-api/docs/llms.txt
- https://llmstxt.site/
- https://directory.llmstxt.cloud/
- https://ai.google.dev/gemini-api/docs/caching?lang=python
  - https://ai.google.dev/gemini-api/docs/caching?lang=python#caching-using-openai
- https://llmstxt.org/domains.html
- Documents:
  - `docs/gemini-3/gemini-3-prompting-guide.md`: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide

### Essential tips for long context prompts

- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips#essential-tips-for-long-context-prompts

```
<documents>
  <document index="1">
    <source>annual_report_2023.pdf</source>
    <document_content>
      {{ANNUAL_REPORT}}
    </document_content>
  </document>
  <document index="2">
    <source>competitor_analysis_q2.xlsx</source>
    <document_content>
      {{COMPETITOR_ANALYSIS}}
    </document_content>
  </document>
</documents>

Analyze the annual report and competitor analysis. Identify strategic advantages and recommend Q3 focus areas.
```

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
