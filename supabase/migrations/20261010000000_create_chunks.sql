create extension if not exists vector with schema extensions;

create table public.chunks (
    id bigint generated always as identity primary key,
    source text not null,
    project text,
    term text,
    section text not null,
    content text not null,
    embedding extensions.vector(1536) not null
);

create index chunks_embedding_idx on public.chunks
    using hnsw (embedding extensions.vector_cosine_ops);

-- No policies: only the bot's direct Postgres connection can access the table, not the public API.
alter table public.chunks enable row level security;

create function public.match_chunks(query_embedding extensions.vector(1536), match_count int default 5)
returns table (
    source text,
    project text,
    term text,
    section text,
    content text,
    similarity float
)
language sql stable
set search_path = public, extensions
as $$
    select source, project, term, section, content,
           1 - (embedding <=> query_embedding) as similarity
    from chunks
    order by embedding <=> query_embedding
    limit match_count;
$$;

revoke execute on function public.match_chunks from public, anon, authenticated;
