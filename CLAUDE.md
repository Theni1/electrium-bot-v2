# Electrium Bot

Discord agent that answers questions about the Electrium Mobility design team (University of Waterloo) using RAG over the team's project docs.

## Stack

Python 3.12+ with uv, Supabase Postgres + pgvector, OpenAI (`text-embedding-3-small`). Planned: LangGraph agent with OpenAI, Tavily web search, LangSmith tracing, discord.py, deployed on Railway with Docker.

## Commands

```sh
uv sync                                   # install dependencies
uv run python -m electrium_bot.ingest     # re-embed data/ and replace all rows in chunks
uv run pytest
```

Run from the repo root: `.env` and `data/` are resolved relative to the working directory.

## Layout

- `data/about.md`, `data/projects/<term_code>-<slug>.md`: curated source of truth for the bot. `docs/` is the raw Docusaurus dump; it is gitignored and not used.
- `src/electrium_bot/config.py`: settings loaded from `.env`. Empty values count as unset.
- `src/electrium_bot/embeddings.py`: shared `embed()`. Ingestion and query-time search must use the same model.
- `src/electrium_bot/ingest/chunker.py`: frontmatter + `##` section splitting.
- `src/electrium_bot/ingest/__main__.py`: chunk, embed, replace rows.
- `supabase/migrations/`: schema. Change it by adding a new migration file, never by editing an applied one.

## Data format

Each project file has YAML frontmatter (`name`, `term`, `term_code`, `leads`, optional `subteam_leads`, `members`, `aliases`) and a body where every section starts with `## `. `about.md` has `name` but no `term`. The chunker assumes this format and should fail loudly on files that break it.

## Retrieval design (decided with the user)

- Pure vector RAG over a single `chunks` table. No SQL filters or `WHERE`-based tools and no members/projects tables: questions are expected to be high-level ("what was X about").
- One chunk per `##` section, plus an `Overview` chunk generated from frontmatter. Every chunk's content starts with `Project: <name> (<term>)\nSection: <section>` so sections stay tied to their project.
- `match_chunks(query_embedding, match_count)` returns rows ordered by cosine similarity. Correct matches score around 0.45 to 0.65 with this model, so a "no answer" threshold must be calibrated on real queries, not guessed.
- Ingestion deletes all rows and re-inserts them in one transaction (about 84 chunks, fractions of a cent).

## Supabase

Project `Electrium-Discord-Bot` (ref `yopgpvxqkfgzafvomfds`, us-west-2). RLS is enabled with no policies, so the public API cannot read data; the bot connects directly via `DATABASE_URL` (session pooler, `aws-1-us-west-2.pooler.supabase.com`).

## Roadmap

Done: project setup, schema, ingestion. Skipped: standalone retrieval CLI.
Next: LangGraph agent (`search_docs`, plus `web_search` for general technical questions only, never for Electrium facts; answer only from tool results, cite sources, say "I don't know" otherwise), evals, per-thread memory, Discord bot (`#ask-electrium` channel with one thread per question, plus `/ask`), Railway deployment.

## Working style

- Build one file at a time. Explain it and let the user review before running or committing.
- Commit after each verified step with conventional commit messages. Never push without asking.
- Never read or print `.env` values.
- Keep code minimal and match existing style: no docstrings, `#` comments only for non-obvious reasons.
