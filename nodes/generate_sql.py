from config import llm

def generate_sql(state):

    question = state["question"]
    schema = state["schema"]

    prompt = f"""
You are a senior MySQL engineer.

Question:
{question}

Schema:
{schema}

Return ONLY SQL.

DO NOT:
- use markdown
- use ```sql
- explain anything

Return raw SQL only.
"""

    response = llm.invoke(prompt)
    sql = response.content

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return {
        "sql": sql
    }