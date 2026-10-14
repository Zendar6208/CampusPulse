# CampusPulse

**Discover opportunities beyond your campus.**

CampusPulse is an open-source project designed to help college students discover hackathons, competitions, workshops, fests, conferences, and other college events in one place.

The long-term vision is to build a trusted campus event network where students can discover opportunities across colleges, while verified student organizations and organizers can publish and manage their events.

> **Current Status:** Active Development — Python CLI Prototype

---

## Why CampusPulse?

College events and opportunities are often scattered across Instagram, WhatsApp groups, Telegram channels, college websites, and individual registration platforms.

This makes discovering relevant opportunities unnecessarily difficult, especially for students interested in participating in events outside their own institutions.

CampusPulse aims to solve this by building a centralized, accessible platform for campus opportunities.

## Current Goal

The immediate objective is to build a functional, reliable, and maintainable foundation for CampusPulse.

Development is incremental, with each stage introducing new software engineering concepts while improving the existing application.

The focus is on building working software rather than accumulating disconnected features.

## Current Features

The current Python-based prototype supports:

### Event Management

* Display available events.
* Search events by name.
* Case-insensitive event searching.
* Add new events.
* View event information.
* Manage event capacity and registration counts.

### Registration Management

* Register participants for events.
* Cancel existing registrations.
* Detect full events.
* Prevent registrations beyond event capacity.
* Prevent registration counts from becoming negative.
* Persist registration changes.

### Data Persistence

* Store events using JSON.
* Automatically load events at startup.
* Save event changes to persistent storage.
* Convert event objects into dictionaries.
* Reconstruct event objects from JSON data.

### Validation and Reliability

* Validate event data types and values.
* Validate event capacity and registration counts.
* Handle missing `events.json` files.
* Handle malformed JSON data.
* Validate the structure of loaded JSON.
* Skip invalid individual event records.
* Preserve valid records when other records are invalid.
* Continue application execution after recoverable loading errors.

## Event Data Model

Each event currently contains:

| Attribute  | Description                     |
| ---------- | ------------------------------- |
| Name       | Name of the event               |
| Category   | Type of event                   |
| Date       | Event date                      |
| Location   | Event venue                     |
| Capacity   | Maximum number of registrations |
| Registered | Current registration count      |

Events are represented internally using an object-oriented `Event` class.

## Technology

The current prototype uses:

* Python 3
* JSON for persistent storage
* Object-Oriented Programming
* Python exception handling
* Git and GitHub for version control

No external Python dependencies are currently required.

## Getting Started

### Requirements

* Python 3.x
* Git (for cloning the repository)

### Installation

Clone the repository:

```bash
git clone https://github.com/Zendar6208/CampusPulse.git
```

Navigate into the project:

```bash
cd CampusPulse
```

Run the application:

```bash
python main
```

### Available Menu

```text
Hackathon Event Management System

1. Display Events
2. Search Event
3. Add Event
4. Register for Event
5. Cancel Registration
6. Exit
```

The application uses `events.json` for persistent event storage.

## Project Structure

```text
CampusPulse/
│
├── main
├── events.json
├── README.md
├── LICENSE
└── .gitignore
```

The structure will evolve as the project grows.

## Development Status

### Implemented

* [x] Basic event management
* [x] Event display and searching
* [x] Case-insensitive event search
* [x] Event creation
* [x] JSON-based persistent storage
* [x] Object-oriented event representation
* [x] Event serialization and deserialization
* [x] Input and state validation
* [x] Event registration
* [x] Registration cancellation
* [x] Capacity validation
* [x] Reusable event lookup
* [x] Registration persistence
* [x] Missing-file handling
* [x] Malformed JSON handling
* [x] Individual invalid-record handling
* [x] Preservation of valid events during loading failures
* [x] Manual edge-case and failure testing

### Next Development Priorities

* [ ] Automated unit testing
* [ ] Improved project organization
* [ ] Further separation of application logic and CLI interactions
* [ ] Additional event-management capabilities
* [ ] Improved documentation

## Project Vision

The planned full platform includes:

* Student accounts.
* College email verification.
* College profiles.
* Verified student organizations.
* Organizer accounts.
* Event creation and management.
* Event registration.
* Advanced event search and filtering.
* Cross-college event discovery.
* Personalized event recommendations.
* Open-source community contributions.

**These are planned capabilities and are not part of the current CLI prototype.**

---

# Development Log

### Day 1 — Initial Prototype

* Created the initial Python-based event management system.
* Implemented event display, searching, and creation.
* Added basic input validation.
* Introduced case-insensitive searching.

### Day 2 — Persistent Event Storage

* Introduced JSON-based event storage.
* Implemented `load_events()` and `save_events()`.
* Connected event creation to persistent storage.
* Verified that events remain available after restarting the application.

### Day 3 — Error Handling & Data Validation

* Added missing-file handling using `FileNotFoundError`.
* Added malformed JSON handling using `json.JSONDecodeError`.
* Validated the structure of stored event data.
* Improved application reliability.

### Day 4 — Introduction to OOP

* Introduced the `Event` class.
* Learned classes, objects, `self`, and `__init__()`.
* Added instance attributes and methods.
* Began transitioning from dictionary-based event representation to objects.

### Day 5 — OOP Integration & Event Behavior

* Integrated `Event` objects into the application.
* Implemented `to_dict()` and `from_dict()`.
* Refactored event display and searching.
* Added registration functionality.
* Introduced `is_full()` for capacity checking.
* Implemented reusable event lookup through `find_event_by_name()`.
* Connected registration changes to JSON persistence.

### Day 6 — Validation, State Management & Robustness

* Added event data type and value validation.
* Prevented invalid capacity and registration counts.
* Used specific exceptions for invalid data.
* Implemented `cancel_registration()`.
* Added registration cancellation to the CLI.
* Improved separation between event behavior and user interaction.
* Tested registration and cancellation persistence.

### Day 7 — Exception Handling & Failure Testing

* Strengthened exception handling during event loading.
* Tested missing and malformed JSON files.
* Improved handling of invalid stored event data.
* Verified application behavior under failure conditions.

### Day 8 — Reliable Event Loading & Edge-Case Testing

**Objective:** Prevent one invalid event record from interrupting the entire event-loading process.

* Reviewed registration and cancellation logic.
* Verified capacity checking using `registered >= capacity`.
* Tested registration boundary conditions.
* Identified an issue where one invalid event could interrupt loading and discard valid records.
* Refactored `load_events()` to handle individual event conversion errors inside the loading loop.
* Added validation to ensure the JSON root contains a list.
* Preserved successfully loaded events when another record was invalid.
* Tested an invalid event containing 501 registrations against a capacity of 100.
* Confirmed that the invalid record was skipped while 10 valid events loaded successfully.
* Verified that CampusPulse continued running normally after encountering invalid data.
### Day 9 — Introduction to Automated Unit Testing

* Introduced Python's built-in `unittest` framework.
* Created `test_event.py` to test the `Event` class independently.
* Used `setUp()` to initialize fresh test objects.
* Implemented six automated tests covering:

  * Successful event registration.
  * Registration rejection when an event is full.
  * Successful registration cancellation.
  * Cancellation rejection when no participants are registered.
  * Full-event detection.
  * Detection of events with available capacity.
* Used `assertTrue()`, `assertFalse()`, and `assertEqual()` to verify expected behavior.
* Successfully executed all six tests.

**Result:** 6 tests passed.

**Key Learning:** A recoverable failure in one record should not prevent unrelated valid records from being processed.

---

## Contributing

CampusPulse is intended to become an open-source project.

Development is currently focused on building and testing the core application. Formal contribution guidelines will be introduced as the project matures.

Ideas, bug reports, suggestions, and pull requests are welcome.

## Development Philosophy

CampusPulse is being built incrementally, alongside the developer's software engineering journey.

The principles guiding development are:

* Understand the code being written.
* Prioritize functionality over unnecessary complexity.
* Introduce technologies when they solve actual problems.
* Test existing behavior before adding new features.
* Learn from bugs rather than simply suppressing errors.
* Build toward a maintainable and genuinely usable product.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Maintainer

**Darsh Agarwal**

CampusPulse — An open-source project built to make discovering college opportunities easier.
