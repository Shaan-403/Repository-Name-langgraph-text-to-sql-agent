from config import llm
from tools.toolkit import tools


list_tables_tool = next(
    tool for tool in tools    
    if tool.name == "sql_db_list_tables"
)


def select_tables(state):
    question = state["question"]
    table = list_tables_tool.invoke("")
    prompt = f"""
User Question:

{question}

Available Tables:

{table}

Return only relevant table names.
Example:
customers,orders,payments

Do not explain.
Do not use bullet points.
Do not use numbering.
"""

    response = llm.invoke(prompt)

    return {
        "selected_tables": response.content.strip()
    }