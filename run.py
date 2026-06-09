from graph import graph


def run_agent(question):

    events = []

    final_state = None

    for event in graph.stream(
        {
            "question": question
        }
    ):

        node_name = list(event.keys())[0]

        events.append(node_name)

    final_state = graph.invoke(
        {
            "question": question
        }
    )

    return events, final_state