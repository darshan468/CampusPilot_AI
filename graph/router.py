def route_query(query):
    
    query = query.lower()

    agents = []

    if any(word in query for word in [
        "study",
        "exam",
        "revision"
    ]):

        agents.append("study")

    if any(word in query for word in [
        "assignment",
        "project",
        "homework"
    ]):

        agents.append("assignment")

    if any(word in query for word in [
        "timetable",
        "class",
        "schedule"
    ]):

        agents.append("timetable")

    if any(word in query for word in [
        "placement",
        "resume",
        "interview"
    ]):

        agents.append("placement")

    if any(word in query for word in [
        "career",
        "roadmap"
    ]):

        agents.append("career")

    if any(word in query for word in [
        "event",
        "hackathon"
    ]):

        agents.append("event")

    if not agents:

        agents.append("chat")

    return agents