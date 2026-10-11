from openai import OpenAI

from electrium_bot.config import settings

EMBEDDING_MODEL = "text-embedding-3-small"

client = OpenAI(api_key=settings.openai_api_key)


def embed(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(model=EMBEDDING_MODEL, input=texts)
    return [item.embedding for item in response.data]
