from pathlib import Path

import pyperclip
from loguru import logger

from utils import prepare_context

DOCS = Path("docs") / "gemini-3"
TASK = "Adapt the prompt to follow the guidelines."

if __name__ == "__main__":
    context = prepare_context(DOCS)
    task = f"<task>\n{TASK}\n</task>"
    input_prompt = "<prompt>\n\n</prompt>"

    prompt = f"{context}\n\n{task}\n\n{input_prompt}"

    pyperclip.copy(prompt)
    logger.info("Copied to clipboard!")
