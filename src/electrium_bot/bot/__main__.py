import discord
from langchain_core.messages import HumanMessage

from electrium_bot.agent.graph import graph
from electrium_bot.config import settings

DISCORD_MESSAGE_LIMIT = 2000
THREAD_NAME_LIMIT = 100

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents, allowed_mentions=discord.AllowedMentions.none())


@client.event
async def on_ready() -> None:
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author.bot or message.channel.id != settings.discord_ask_channel_id:
        return
    question = message.content.strip()
    if not question:
        return

    thread = await message.create_thread(name=question[:THREAD_NAME_LIMIT])
    async with thread.typing():
        result = await graph.ainvoke({"messages": [HumanMessage(question)]})
    await thread.send(result["messages"][-1].content[:DISCORD_MESSAGE_LIMIT])


def main() -> None:
    client.run(settings.discord_token)


if __name__ == "__main__":
    main()
