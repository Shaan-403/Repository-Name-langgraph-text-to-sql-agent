FORBIDDEN = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE"
]
def sql_guard(state):

    sql = state["sql"].upper()

    for keyword in FORBIDDEN:

        if keyword in sql:

            return {
                "guard_failed": True
            }

    return {
        "guard_failed": False
    }