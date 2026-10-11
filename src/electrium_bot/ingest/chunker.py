from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class Chunk:
    source: str
    project: str | None
    term: str | None
    section: str
    content: str


def parse_file(path: Path) -> tuple[dict, str]:
    _, frontmatter, body = path.read_text().split("---\n", 2)
    return yaml.safe_load(frontmatter), body


def split_sections(body: str) -> list[tuple[str, str]]:
    sections = []
    for line in body.splitlines():
        if line.startswith("## "):
            sections.append((line[3:].strip(), []))
        elif sections:
            sections[-1][1].append(line)
    return [(title, "\n".join(lines).strip()) for title, lines in sections]

def overview(meta: dict) -> str:
    led_by = f" led by {', '.join(meta['leads'])}" if meta["leads"] else ""
    lines = [f"{meta['name']} was a {meta['term']} project{led_by}."]
    if aliases := meta.get("aliases"):
        lines.append(f"Also known as: {', '.join(aliases)}.")
    for team, names in meta.get("subteam_leads", {}).items():
        lines.append(f"{team} lead: {', '.join(names)}.")
    for team, names in meta.get("members", {}).items():
        label = "Team members" if team == "Team" else f"{team} team"
        lines.append(f"{label}: {', '.join(names)}.")
    return "\n".join(lines)


def chunk_file(path: Path) -> list[Chunk]:
    meta, body = parse_file(path)
    term = meta.get("term")
    sections = split_sections(body)

    if term:
        sections.insert(0, ("Overview", overview(meta)))
        header = f"Project: {meta['name']} ({term})"
    else:
        header = meta["name"]

    return [
        Chunk(
            source=path.name,
            project=meta["name"] if term else None,
            term=term,
            section=title,
            content=f"{header}\nSection: {title}\n\n{text}",
        )
        for title, text in sections
    ]


def chunk_all(data_dir: Path) -> list[Chunk]:
    paths = [data_dir / "about.md", *sorted((data_dir / "projects").glob("*.md"))]
    return [chunk for path in paths for chunk in chunk_file(path)]
