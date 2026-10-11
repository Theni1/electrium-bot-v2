import psycopg
from langchain_core.tools import tool

from electrium_bot.config import settings
from electrium_bot.embeddings import embed

MATCH_COUNT = 5

@tool(
    description=(
        "Search Electrium Mobility's documentation: project descriptions, features, specs, "
        "team members, and general team info (joining, sponsors, contact). Use it for any "
        "question about Electrium or its projects. Pass a short, specific search phrase."
    )
)
def search_docs(query: str) -> str:
    [query_embedding] = embed([query])

    with psycopg.connect(settings.database_url) as conn:
        rows = conn.execute(
            "select content from match_chunks(%s::extensions.vector, %s)",
            (str(query_embedding), MATCH_COUNT),
        ).fetchall()

    if not rows:
        return "No matching documents found."
    return "\n\n---\n\n".join(content for (content,) in rows)
