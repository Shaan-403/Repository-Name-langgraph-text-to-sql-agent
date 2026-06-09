from nodes.select_tables import select_tables
from nodes.get_schema import get_schema
from nodes.generate_sql import generate_sql
from nodes.execute_sql import execute_sql
from nodes.repair_sql import repair_sql
from nodes.generate_answer import generate_answer
from nodes.sql_guard import sql_guard
from nodes.blocked_response import blocked_response
from state import AgentState
from langgraph.graph import (
    StateGraph,
    START,
    END
)


def route_after_execute(state):

    if state.get("error"):
        return "repair_sql"

    return "generate_answer"

def route_after_guard(state):

    if state["guard_failed"]:
        return "blocked"

    return "execute_sql"


builder = StateGraph(
    AgentState
)

builder.add_node(
    "select_tables",
    select_tables
)

builder.add_node(
    "get_schema",
    get_schema
)

builder.add_node(
    "generate_sql",
    generate_sql
)

builder.add_node(
    "execute_sql",
    execute_sql
)

builder.add_node(
    "repair_sql",
    repair_sql
)

builder.add_node(
    "generate_answer",
    generate_answer
)

from nodes.sql_guard import sql_guard

builder.add_node(
    "sql_guard",
    sql_guard
)



builder.add_node(
    "blocked_response",
    blocked_response
)









builder.add_edge(
    START,
    "select_tables"
)


builder.add_edge(
    "select_tables",
    "get_schema"
)

builder.add_edge(
    "get_schema",
    "generate_sql"
)
builder.add_edge(
    "generate_sql",
    "sql_guard"
)

builder.add_conditional_edges(
    "sql_guard",
    route_after_guard,
    {
        "blocked": "blocked_response",
        "execute_sql": "execute_sql",
    }
)

builder.add_conditional_edges(
    "execute_sql",
    route_after_execute,
    {
        "repair_sql": "repair_sql",
        "generate_answer": "generate_answer",
    }
)
builder.add_edge(
    "blocked_response",
    END
)

builder.add_edge(
    "repair_sql",
    "execute_sql"
)

builder.add_edge(
    "generate_answer",
    END
)

graph = builder.compile()

from IPython.display import Image, display
png_data = graph.get_graph().draw_mermaid_png()

with open("graph.png", "wb") as f:
    f.write(png_data)