import streamlit as st

from run import run_agent
from database.history import (
    save_query,
    get_recent_queries
)




st.set_page_config(
    page_title="Text-to-SQL Agent",
    layout="wide"
)

st.title("🤖 Text-to-SQL Agent")
st.sidebar.title("📜 Query History")

history = get_recent_queries()

# for question_text, created_at in history:

#     st.sidebar.caption(created_at)

#     st.sidebar.write(question_text)

#     st.sidebar.divider()
for question_text, sql_query, created_at in history:

    with st.sidebar.expander(question_text):

        st.caption(created_at)

        st.code(
            sql_query,
            language="sql"
        )

question = st.text_input(
    "Ask a question"
)

if st.button("Run") and question:

    events, result = run_agent(question)
    save_query(
    question,
    result.get("sql", ""),
    result.get("answer", "")
    )

    LABELS = {
        "select_tables": "Selecting relevant tables",
        "get_schema": "Fetching schema",
        "generate_sql": "Generating SQL",
        "sql_guard": "Validating SQL",
        "execute_sql": "Executing query",
        "repair_sql": "Repairing failed SQL",
        "generate_answer": "Generating answer",
        "blocked_response": "Blocking unsafe query"
    }

    st.subheader("Agent Activity")

    for event in events:

        st.success(
            LABELS.get(event, event)
        )

    st.divider()

    st.subheader("Generated SQL")

    st.code(
        result.get("sql", ""),
        language="sql"
    )

    st.subheader("Answer")

    st.success(
        result.get("answer", "")
    )