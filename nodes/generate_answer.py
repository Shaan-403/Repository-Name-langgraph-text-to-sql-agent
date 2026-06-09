from config import llm

def generate_answer(state):

    if state["result"] in ["[]", "", None]:

        return {
            "answer":
            "No matching records were found."
        }
    prompt = f"""
    Question:
    {state['question']}

    Result:
    {state['result']}

    Answer naturally.
    Use ₹ instead of $.
    """

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }