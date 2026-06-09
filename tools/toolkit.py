from langchain_community.agent_toolkits import SQLDatabaseToolkit

from database.mysql_connection import db
from config import llm

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=llm
)

tools = toolkit.get_tools()


for tool in tools:
    print(tool.name)