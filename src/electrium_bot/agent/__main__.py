from langchain_core.messages import HumanMessage

from electrium_bot.agent.graph import graph


def main() -> None:
    print("Ask about Electrium. Type 'quit' to exit.")
    while True:
        try:
            question = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if question.lower() in {"quit", "exit"}:
            break
        if not question:
            continue

        result = graph.invoke({"messages": [HumanMessage(question)]})

        for message in result["messages"]:
            for call in getattr(message, "tool_calls", []):
                print(f"  [{call['name']}: {call['args']}]")
        print(f"\nBot: {result['messages'][-1].content}")


if __name__ == "__main__":
    main()
