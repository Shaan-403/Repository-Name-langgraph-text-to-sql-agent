from tools.toolkit import tools

schema_tool = next(
    tool for tool in tools
    if tool.name == "sql_db_schema"
)

def get_schema(state):

    schema = schema_tool.invoke(
        state["selected_tables"]
    )
    
    return {
        "schema": schema
    }