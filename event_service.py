from event import Event
import event


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

def create_event(events, name, category, date, location, capacity):
    if not isinstance(events, list):
        raise TypeError("events must be a list")

    if not isinstance(name, str) or not isinstance(category, str) or not isinstance(date, str) or not isinstance(location, str) or not isinstance(capacity, int):
        raise TypeError("Invalid input types for event creation.")

    if capacity < 0:
        raise ValueError("Event capacity cannot be negative.")
    event = Event(name, category, date, location, capacity, 0)
    name = name.strip()

    if find_event_by_name(events, name) is not None:
        raise ValueError("An event with this name already exists.")

    event = Event(name, category, date, location, capacity, 0)
    events.append(event)

    return event


def register_for_event(events,event_name):
    if not isinstance(events,list):
        raise TypeError("events must be a list")
    if not isinstance(event_name,str):
        raise TypeError("event_name must be a string")
    event = find_event_by_name(events,event_name)
    if event is None:
        return False
    return event.register()

def cancel_event_registration(events,event_name):
    if not isinstance(events,list):
        raise TypeError("events must be a list")
    
    if not isinstance(event_name,str):
        raise TypeError("event_name must be a string")
    event = find_event_by_name(events,event_name)
    if event is None:
        return False
    return event.cancel_registration()

def update_event(events, event_name, new_location):
    if not isinstance(events, list):
        raise TypeError("events must be a list")
    if not isinstance(event_name, str):
        raise TypeError("event_name must be a string")
    if not isinstance(new_location, str):
        raise TypeError("new_location must be a string")

    event = find_event_by_name(events, event_name)

    if event is None:
        return False

    new_location = new_location.strip()

    if not new_location:
        raise ValueError("Event location cannot be empty.")

    event.location = new_location
    return True

def update_event_capacity(events, event_name, new_capacity):
    if not isinstance(events, list):
        raise TypeError("events must be a list")
    if not isinstance(event_name, str):
        raise TypeError("event_name must be a string")
    if type(new_capacity) is not int:
        raise TypeError("new_capacity must be an integer")
    if new_capacity < 0:
        raise ValueError("Event capacity cannot be negative.")

    event = find_event_by_name(events, event_name)
    if event is None:
        return False

    if new_capacity < event.registered:
        raise ValueError("Capacity cannot be below existing registrations.")

    event.capacity = new_capacity
    return True
    
    