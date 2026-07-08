from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DOCS_PATH = BASE_DIR / "knowledge_base" / "docs"


def retrieve(query: str):

    query = query.lower()

    matched_context = []

    for file in DOCS_PATH.glob("*.txt"):

        with open(file, "r", encoding="utf-8") as f:

            content = f.read()

            if any(word in content.lower() for word in query.split()):
                matched_context.append(content)

    # If nothing matches, return all knowledge
    if not matched_context:

        for file in DOCS_PATH.glob("*.txt"):

            with open(file, "r", encoding="utf-8") as f:
                matched_context.append(f.read())

    return "\n\n".join(matched_context)