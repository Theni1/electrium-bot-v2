from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from electrium_bot.agent.prompts import SYSTEM_PROMPT
from electrium_bot.agent.tools import search_docs
from electrium_bot.config import settings

CHAT_MODEL = "gpt-5.4-mini"
TOOLS = [search_docs]

model = ChatOpenAI(model=CHAT_MODEL, api_key=settings.openai_api_key).bind_tools(TOOLS)


def agent(state: MessagesState) -> dict:
    response = model.invoke([SystemMessage(SYSTEM_PROMPT), *state["messages"]])
    return {"messages": [response]}


builder = StateGraph(MessagesState)
builder.add_node("agent", agent)
builder.add_node("tools", ToolNode(TOOLS))
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

# Caps agent/tool round trips so a confused model can't loop forever on our API bill.
graph = builder.compile().with_config(recursion_limit=10)
