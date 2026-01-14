from pathlib import Path
from textwrap import indent


def prepare_context(docs: Path) -> str:
    xml_docs: list[str] = []

    for index, doc in enumerate(docs.glob("*.md"), start=1):
        content = doc.read_text().strip()
        indented_content = indent(content, " " * 2)

        xml_doc = f'<document index="{index}">\n{indented_content}\n</document>'
        xml_docs.append(xml_doc)

    all_docs = indent("\n".join(xml_docs), " " * 2)

    return f"<context>\n{all_docs}\n</context>"


def ensure_file(file: Path, content: str | None = None) -> None:
    file.parent.mkdir(parents=True, exist_ok=True)

    if not file.exists():
        file.write_text(content if content is not None else "")
