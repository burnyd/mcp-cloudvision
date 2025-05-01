import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage
import os

# Ensure you have GOOGLE_API_KEY environment variable set
google_api_key = os.getenv("GEMINI_API_KEY")
if not google_api_key:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    exit()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17", google_api_key=google_api_key)
server_params = StdioServerParameters(
    command="python3",
    # Make sure to update to the full absolute path to your math_server.py file
    args=["cvpserver.py"],
)

async def run_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create the agent
            agent = create_react_agent(model, tools)

            print("Welcome to the chat! Type 'exit' to quit.")
            while True:
                user_input = input("You: ")
                if user_input.lower() == "exit":
                    break

                agent_response = await agent.ainvoke({"messages": user_input})
                ai_messages = [msg for msg in agent_response['messages'] if isinstance(msg, AIMessage) and msg.content]

                if ai_messages:
                    final_answer = ai_messages[-1].content
                    print(f"The final answer is: {final_answer}")
                else:
                    print("No AIMessage with content found.")

if __name__ == "__main__":
    asyncio.run(run_agent())