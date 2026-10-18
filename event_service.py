def find_event_by_name(events, search_name):
    if not isinstance(events, list):
        raise TypeError("events must be a list")

    search_name = search_name.strip()

    if not search_name:
        return None

    for event in events:
        if event.name.casefold() == search_name.casefold():
            return event

    return None