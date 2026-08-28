# 🤖 LangGraph Text-to-SQL Agent

An Agentic AI application that converts natural language questions into executable SQL queries using LangGraph, LangChain, OpenAI, and MySQL.

The system automatically discovers relevant tables, analyzes database schema, generates SQL, validates query safety, executes against a live database, repairs failed queries, and produces human-readable answers.

---

## 🚀 Features

### Natural Language to SQL

Convert business questions into SQL without manually writing queries.

**Example**

**Input**

```text
Which customer spent the highest amount?
```

**Generated SQL**

```sql
SELECT c.customer_id,
       CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       SUM(p.amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments p ON o.order_id = p.order_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 1;
```

---

### Agentic Workflow using LangGraph

The application is built as a graph-based workflow instead of a traditional linear script.

```text
START
  ↓
select_tables
  ↓
get_schema
  ↓
generate_sql
  ↓
sql_guard
  ↓
      ?
   ┌──┴────┐
   │       │
 BLOCK   EXECUTE
   │       │
   ▼       ▼
blocked  execute_sql
             │
             ▼
              ?
          ┌──┴──┐
          │     │
      SUCCESS ERROR
          │     │
          ▼     ▼
     generate  repair_sql
      answer       │
                   ▼
              execute_sql
```

---

### Schema-Aware Query Generation

The agent dynamically:

* Discovers available tables
* Selects relevant tables
* Fetches table schemas
* Generates SQL using real schema information

This significantly improves SQL accuracy.

---

### SQL Safety Guard

The application prevents execution of destructive queries.

Blocked operations:

```sql
DELETE
DROP
UPDATE
ALTER
TRUNCATE
INSERT
```

Unsafe queries are intercepted before reaching the database.

---

### Self-Healing SQL Execution

If generated SQL fails:

1. Error is captured
2. Error message is passed back to the LLM
3. SQL is automatically repaired
4. Query is executed again

This creates a genuine agent loop instead of a simple request-response workflow.

---

### Agent Activity Tracking

The UI displays each execution step:

```text
✓ Selecting relevant tables

✓ Fetching schema

✓ Generating SQL

✓ Validating SQL

✓ Executing query

✓ Generating answer
```

This improves transparency and debugging.

---

### Query History

Every query is stored locally.

Stored data:

* User Question
* Generated SQL
* Final Answer
* Timestamp

Allows users to revisit previous analyses.

---

### LangSmith Observability

Integrated with LangSmith for:

* Trace visualization
* Node-level debugging
* LLM monitoring
* Execution analysis
* Agent observability

Provides full visibility into agent execution.

---

## 🏗️ Architecture

### Agent Nodes

| Node             | Responsibility                     |
| ---------------- | ---------------------------------- |
| select_tables    | Select relevant tables             |
| get_schema       | Fetch schema information           |
| generate_sql     | Generate SQL query                 |
| sql_guard        | Validate SQL safety                |
| execute_sql      | Execute query                      |
| repair_sql       | Repair failed SQL                  |
| generate_answer  | Generate natural language response |
| blocked_response | Handle unsafe queries              |

---

## 🧠 Agent State

The workflow uses a shared state object:

```python
class AgentState(TypedDict):
    question: str
    selected_tables: str
    schema: str
    sql: str
    result: str
    answer: str
    error: str
    guard_failed: bool
```

Each node reads and updates the shared state.

---

## 🛠️ Tech Stack

### AI & Agent Framework

* LangGraph
* LangChain
* OpenAI GPT Models
* LangSmith

### Backend

* Python
* SQLAlchemy
* MySQL

### Frontend

* Streamlit

### Database

* MySQL Order Management Database
* 8 relational tables
* Production-style schema
* Foreign key constraints
* Sample business data

---

## 📂 Project Structure

```text
text-to-sql-agent/

├── app.py
├── graph.py
├── run.py
├── state.py

├── nodes/
│   ├── select_tables.py
│   ├── get_schema.py
│   ├── generate_sql.py
│   ├── sql_guard.py
│   ├── execute_sql.py
│   ├── repair_sql.py
│   ├── generate_answer.py
│   └── blocked_response.py

├── database/
│   ├── history.py
│   └── order_management.sql

├── tools/
│   └── toolkit.py

├── screenshots/

├── requirements.txt
├── .env.example
└── README.md
```



---

## 🔍 Example Questions

```text
Which customer spent the highest amount?

Show top 5 customers by total spend.

Find customers who have never reviewed an order.

Show failed payment transactions.

What is the average order value?

List products generating the highest revenue.

Show customers with more than 5 orders.
```

---

## 🎯 Key Engineering Decisions

### Why LangGraph?

Traditional workflow:

```text
Question
   ↓
SQL
   ↓
Answer
```

LangGraph workflow:

```text
Question
   ↓
Generate SQL
   ↓
Validate
   ↓
Execute
   ↓
Repair if needed
   ↓
Answer
```

This enables retries, routing, and agentic decision-making.

---

### Why SQL Guard?

LLMs can generate destructive SQL.

The safety layer ensures:

* Database integrity
* Read-only access
* Safe production behavior

---

### Why LangSmith?

Provides production-grade observability:

* Execution traces
* Debugging
* Monitoring
* Performance analysis

---

## 🚀 Future Improvements

* CSV export
* Multi-database support
* Authentication & RBAC
* Query caching
* Role-based SQL permissions
* Docker deployment
* Cloud deployment
* Human-in-the-loop approvals

---

## 👨‍💻 Author

Built to explore Agentic AI systems using LangGraph, LangChain, OpenAI, and MySQL while applying production-oriented engineering practices such as observability, validation, safety, and workflow orchestration.
