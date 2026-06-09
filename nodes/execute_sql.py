from tools.toolkit import tools

query_tool = next(
    tool for tool in tools
    if tool.name == "sql_db_query"
)

def execute_sql(state):


    sql = state["sql"]

    try:
        result = query_tool.invoke(sql)
        return {
            "result": result,
            "error": None
        }
    except Exception as e:
        result = str(e)
        return {
            result: "",
            "error": result
        }
