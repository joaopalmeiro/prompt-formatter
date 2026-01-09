from pathlib import Path

import pyperclip
from loguru import logger

from utils import prepare_context

DOCS = Path("docs") / "gemini-3"

TASK = "Adapt the prompt to follow the guidelines."

# Source: https://ai.google.dev/gemini-api/docs/prompting-strategies#structured_prompting_examples
OUTPUT_FORMAT = "Return a single code block."

if __name__ == "__main__":
    context = prepare_context(DOCS)
    task = f"<task>\n{TASK}\n</task>"
    input_prompt = "<prompt>\n\n</prompt>"
    output_format = f"<output_format>\n{OUTPUT_FORMAT}\n</output_format>"

    prompt = f"{context}\n\n{task}\n\n{input_prompt}\n\n{output_format}"

    pyperclip.copy(prompt)
    logger.info("Copied to clipboard!")
