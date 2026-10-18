import json
from event import Event
def load_events(filename="events.json"):
    events = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: events.json is not a valid JSON file.")
        return []

    if not isinstance(data, list):
        print("Error: events.json does not contain a valid list of events.")
        return []

    for event in data:
        try:
            events.append(Event.from_dict(event))
        except (TypeError, ValueError, KeyError) as error:
            print(f"Skipping invalid event data: {error}")
    

    return events


def save_events(events, filename="events.json"):
    event_data = []

    for event in events:
        try:
            event_data.append(event.to_dict())
        except (AttributeError, TypeError, ValueError) as error:
            print(f"Skipping invalid event: {error}")

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(event_data, file, indent=4)
