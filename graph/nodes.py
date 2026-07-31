from graph.router import route_query


def supervisor_node(state):

    state["agent"] = route_query(state["query"])

    return state


def study_node(state):

    state["response"] = "📚 Study Agent Selected."

    return state


def assignment_node(state):

    state["response"] = "📝 Assignment Agent Selected."

    return state


def timetable_node(state):

    state["response"] = "📅 Timetable Agent Selected."

    return state


def placement_node(state):

    state["response"] = "💼 Placement Agent Selected."

    return state


def career_node(state):

    state["response"] = "🎯 Career Agent Selected."

    return state


def event_node(state):

    state["response"] = "📢 Event Agent Selected."

    return state


def chat_node(state):

    state["response"] = "🤖 General AI Chat."

    return state