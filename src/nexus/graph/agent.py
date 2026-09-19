from langchain_openai import ChatOpenAI
from nexus.config import settings
from nexus.graph.state import State
from nexus.graph.tools import get_current_date_and_time, flip_coin, roll_dice

# LLM instance with default tools
model = ChatOpenAI(model=settings.model_name, api_key=settings.openai_api_key)
model_with_tools = model.bind_tools(tools=[get_current_date_and_time, flip_coin, roll_dice])


# Agent node for Graph
def agent_node(state: State) -> dict:
    """
    Graph Node responsible for chatbot interaction with LLM
    """
    agent_response = model_with_tools.invoke(state["messages"])
    return {"messages": [agent_response]}
