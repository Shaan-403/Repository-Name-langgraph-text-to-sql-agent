from typing import TypedDict

class AgentState(TypedDict):

    question: str

    selected_tables: str

    schema: str

    sql: str

    result: str

    answer: str

    error: str
    
    guard_failed: bool