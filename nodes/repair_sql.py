from config import llm
from tools.toolkit import tools


def repair_sql(state):
    bad_sql = state["sql"]
    error_message = state["error_message"]
    tables = state["schema"]

    fix_prompt = f"""The following SQL query is invalid and causes an error when executed: {bad_sql}. The error message is: {error_message}. The tables in the database are: {tables}. Please fix the SQL query so that it is valid and can be executed without errors. Only return the
    fixed SQL query, do not include any explanations."""
    
    fixed_sql = llm.invoke(fix_prompt)
    return {
        "sql": fixed_sql.content
    }