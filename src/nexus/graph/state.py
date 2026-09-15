from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages


# Custom state class for Graph
class State(TypedDict):
    messages: Annotated[list, add_messages]
