from storage import load_events, save_events
from event import Event
from event_service import find_event_by_name, create_event, register_for_event

def display_events(events):
    if not isinstance(events, list):
        raise TypeError("events must be a list")
    if not events:
        print("No events to display.")
        return

    print("Upcoming Hackathon Events:")

    for event in events:
        event.display()
        print("-" * 30)




def search_event(events):
    """Search for an event by name, display it, and return the matching event."""

    if not isinstance(events, list):
        raise TypeError("events must be a list")

    search_name = input("Enter event name to search: ").strip()

    if not search_name:
        print("Event name cannot be empty.")
        return None

    event = find_event_by_name(events, search_name)

    if event:
        print("Event Found!")
        event.display()
        return event

    print("Event not found.")
    return None


def add_event(events):
    """Add a new event to the events list."""

    if not isinstance(events, list):
        raise TypeError("events must be a list")

    name = input("Enter event name: ").strip()
    category = input("Enter event category: ").strip()
    date = input("Enter event date (DD-MM-YYYY): ").strip()
    location = input("Enter event location: ").strip()
    capacity = input("Enter event capacity: ").strip()

    if not name or not category or not date or not location or not capacity:
        print("All fields are required.")
        return

    try:
        capacity = int(capacity)
    except ValueError:
        print("Capacity must be an integer.")
        return

    try:
        new_event = create_event(
            events,
            name,
            category,
            date,
            location,
            capacity
        )
    except (ValueError, TypeError) as error:
        print(f"Invalid event: {error}")
        return

    

    print(f"Event '{name}' added successfully!")


def main():
    events = load_events()

    while True:
        print("\nHackathon Event Management System")
        print("1. Display Events")
        print("2. Search Event")
        print("3. Add Event")
        print("4. Register for Event")
        print("5. Cancel Registration")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            display_events(events)

        elif choice == '2':
            search_event(events)

        elif choice == '3':
            add_event(events)
            save_events(events)

        elif choice == '4':
            search_name = input("Enter event name to register: ").strip()

            event = find_event_by_name(events, search_name)
            result = register_for_event(events, search_name)

            if event:
                event.display()

                if result:
                    print("Registration successful!")
                    save_events(events)
                else:
                    print("Registration failed. Event is full.")
            else:
                print("Event not found.")

        elif choice == '5':
            search_name = input("Enter event name to cancel registration: ").strip()

            event = find_event_by_name(events, search_name)

            if event:
                event.display()

                if event.cancel_registration():
                    print("Registration cancelled successfully!")
                    save_events(events)
                else:
                    print("Cancellation failed. No registrations found.")
            else:
                print("Event not found.")

        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
