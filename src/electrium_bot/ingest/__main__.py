from pathlib import Path

import psycopg

from electrium_bot.config import settings
from electrium_bot.embeddings import embed
from electrium_bot.ingest.chunker import chunk_all

DATA_DIR = Path("data")


def main() -> None:
    chunks = chunk_all(DATA_DIR)
    embeddings = embed([chunk.content for chunk in chunks])

    rows = [
        (chunk.source, chunk.project, chunk.term, chunk.section, chunk.content, str(embedding))
        for chunk, embedding in zip(chunks, embeddings, strict=True)
    ]
    
    with psycopg.connect(settings.database_url) as conn:
        conn.execute("delete from chunks")
        conn.cursor().executemany(
            """
            insert into chunks (source, project, term, section, content, embedding)
            values (%s, %s, %s, %s, %s, %s::extensions.vector)
            """,
            rows,
        )

    print(f"Ingested {len(rows)} chunks")


if __name__ == "__main__":
    main()
