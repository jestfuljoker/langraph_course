import operator
from typing import Annotated, TypedDict

from langgraph.graph import StateGraph
from rich import print

# def reducer(a: list[str], b: list[str]) -> list[str]:
#     return a + b


# Defining the state
class State(TypedDict):
    nodes_path: Annotated[list[str], operator.add]


# Defining the nodes
def node_a(state: State) -> State:
    output_state: State = {"nodes_path": ["A"]}

    print("> node a", f"{state=}", f"{output_state=}")

    return output_state


def node_b(state: State) -> State:
    output_state: State = {"nodes_path": ["B"]}

    print("> node b", f"{state=}", f"{output_state=}")

    return output_state


# Defining the graph builder
builder = StateGraph(State)

builder.add_node("A", node_a)
builder.add_node("B", node_b)

# Connecting the edges
builder.add_edge("__start__", "A")
builder.add_edge("A", "B")
builder.add_edge("B", "__end__")

# Compile the graph
graph = builder.compile()

# Get result
response = graph.invoke({"nodes_path": []})

print()
print(f"{response=}")
print()
