events = [
    {
        "name": "Origins",
        "category": "Hackathon",
        "date": "28-29 August 2026",
        "location": "Melakottaiyur, India",
        "capacity": 500,
        "registered": 0
    },
    {
        "name": "PEC Hacks 4.0",
        "category": "Hackathon",
        "date": "29-30 August 2026",
        "location": "Panimalar Engineering College, Chennai",
        "capacity": 500,
        "registered": 0
    },
    {
        "name": ".hack '26",
        "category": "Hackathon",
        "date": "4-6 September 2026",
        "location": "India",
        "capacity": 1000,
        "registered": 0
    },
    {
        "name": "ETHKochi",
        "category": "Hackathon",
        "date": "5 September 2026",
        "location": "Kochi, India",
        "capacity": 500,
        "registered": 0
    },
    {
        "name": "VENTURE'26",
        "category": "Hackathon",
        "date": "10 September 2026",
        "location": "India",
        "capacity": 500,
        "registered": 0
    },
    {
        "name": "Metamorph 2.0",
        "category": "Hackathon",
        "date": "12 September 2026",
        "location": "India",
        "capacity": 100,
        "registered": 0
    },
    {
        "name": "DSU DEVHACK 3.0",
        "category": "Hackathon",
        "date": "18 September 2026",
        "location": "India",
        "capacity": 1000,
        "registered": 0
    },
    {
        "name": "WebCraft24",
        "category": "Hackathon",
        "date": "18 September 2026",
        "location": "India",
        "capacity": 100,
        "registered": 0
    },
    {
        "name": "NexHack 2.0",
        "category": "Hackathon",
        "date": "25 September 2026",
        "location": "India",
        "capacity": 1000,
        "registered": 0
    },
    {
        "name": "HackNex Season 2",
        "category": "Hackathon",
        "date": "25 September 2026",
        "location": "India",
        "capacity": 500,
        "registered": 0
    }
]
def display_events():
    print("Upcoming Hackathon Events:")
    for event in events:
        print(f"Name: {event['name']}")
        print(f"Category: {event['category']}")
        print(f"Date: {event['date']}")
        print(f"Location: {event['location']}")
        print(f"Capacity: {event['capacity']}")
        print(f"Registered: {event['registered']}")
        print("-" * 30)
def search_event(events):
    """Search for an event by name, display it, and return the matching event."""
    if not isinstance(events, list):
        raise TypeError("events must be a list")

    search_name = input("Enter event name to search: ").strip()
    if not search_name:
        print("Event name cannot be empty.")
        return None

    for event in events:
        if event.get("name", "").casefold() == search_name.casefold():
            print("Event Found!")
            print(event)
            return event
    else:
        print("Event not found.")
        return None

search_event(events)