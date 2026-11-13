# CampusPulse

### Discover opportunities beyond your campus.

CampusPulse is an open-source project designed to help college students discover hackathons, competitions, workshops, fests, conferences, and other campus opportunities in one place.

The long-term vision is to build a trusted campus event network where students can discover opportunities across colleges, while verified student organizations and organizers can publish and manage their events.

> **Current Status:** Active Development — Python CLI Prototype

---

## Why CampusPulse?

College events and opportunities are scattered across Instagram, WhatsApp groups, Telegram channels, college websites, and individual registration platforms.

This makes discovering relevant opportunities unnecessarily difficult, particularly for students interested in participating in events outside their own institutions.

CampusPulse aims to address this fragmentation by building a centralized platform for campus opportunities.

## Current Goal

The immediate objective is to build a functional, reliable, and maintainable foundation for CampusPulse.

Development is incremental, with an emphasis on modular architecture, input validation, persistent storage, automated testing, and clean separation of responsibilities.

The focus is on building working software rather than accumulating disconnected features.

---

## Features

The current Python CLI prototype supports the following functionality.

### Event Management
- Display all available events.
- Search events by name.
- Case-insensitive event searching.
- Create new events.
- Update event locations.
- Update event capacities.
- Delete events safely.
- Filter events by category.
- Sort events chronologically by date.

### Registration Management
- Register participants for events.
- Cancel existing registrations.
- Detect events that have reached capacity.
- Prevent registrations beyond event capacity.
- Prevent registration counts from becoming negative.
- Preserve registration data during event updates.
- Persist successful registration changes.

### Data Persistence
- Store event data using JSON.
- Automatically load events at application startup.
- Save successful event modifications.
- Serialize event objects into dictionaries.
- Reconstruct event objects from stored JSON data.
- Handle missing and malformed JSON files.
- Validate the structure of loaded JSON data.
- Skip invalid individual event records while preserving valid ones.

### Validation and Reliability
- Validate event data types and values.
- Prevent negative event capacities.
- Prevent registrations from exceeding event capacity.
- Prevent duplicate event names.
- Support case-insensitive duplicate detection.
- Normalize event names and locations.
- Reject invalid event operations.
- Handle recoverable persistence errors.

### Automated Testing
- Unit testing with Python's built-in `unittest` framework.
- Service-layer testing.
- CLI testing using mocked input and persistence.
- Registration and cancellation tests.
- Event creation and deletion tests.
- Capacity validation tests.
- Category filtering tests.
- Chronological sorting tests.
- JSON persistence and error-handling tests.
- Original-data preservation tests.

**Current test suite:** 91 tests, with additional tests introduced as development progresses.

---

## Event Data Model

Each event currently contains six attributes:

| Attribute | Description |
|---|---|
| `name` | Name of the event |
| `category` | Type or category of the event |
| `date` | Event date (`DD-MM-YYYY`) |
| `location` | Event venue |
| `capacity` | Maximum number of registrations |
| `registered` | Current registration count |

Events are represented internally using an object-oriented `Event` class.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core application |
| JSON | Persistent data storage |
| `unittest` | Automated testing |
| `unittest.mock` | Mocking user input and dependencies |
| Git | Version control |
| GitHub | Source code hosting and collaboration |

No external Python dependencies are currently required.

---

## Getting Started

### Requirements

- Python 3.x
- Git (for cloning the repository)

### Installation

Clone the repository:

```bash
git clone https://github.com/Zendar6208/CampusPulse.git
```

Navigate to the project directory:

```bash
cd CampusPulse
```

### Run the Application

```bash
python main.py
```

The application uses `events.json` for persistent event storage.

---

## Available CLI Operations

The current application provides the following menu:

```text
Hackathon Event Management System

1. Display Events
2. Search Event
3. Add Event
4. Register for Event
5. Cancel Registration
6. Update Event Location
7. Update Event Capacity
8. Delete Event
9. Filter Events by Category
10. Exit
```

The event-management functionality is implemented through reusable service functions, keeping application logic separate from terminal interactions.

---

## Project Structure

```text
CampusPulse/
│
├── main.py
├── event.py
├── storage.py
├── event_service.py
│
├── test_event.py
├── test_event_service.py
├── test_main.py
│
├── events.json
├── README.md
├── LICENSE
└── .gitignore
```

### Module Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | CLI interface and application flow |
| `event.py` | Event class, attributes, and event-level operations |
| `storage.py` | JSON loading and saving |
| `event_service.py` | Reusable event-management operations |
| `test_event.py` | Tests for the Event class and persistence |
| `test_event_service.py` | Tests for event-management services |
| `test_main.py` | CLI and application-flow tests |
| `events.json` | Persistent event data |

---

## Running Tests

CampusPulse uses Python's built-in `unittest` framework.

Run the complete test suite:

```bash
python -m unittest discover -v
```

Run individual test modules:

```bash
python -m unittest test_event -v
python -m unittest test_event_service -v
python -m unittest test_main -v
```

Tests use temporary files and mocking where appropriate to avoid unintended modifications to actual application data.

---

## Architecture

CampusPulse follows a modular architecture that separates different application responsibilities.

```text
             User
              |
              v
         main.py
        (CLI Layer)
              |
              v
      event_service.py
       (Service Layer)
              |
        +-----+-----+
        |           |
        v           v
     event.py    storage.py
   (Event Model) (Persistence)
        |           |
        +-----+-----+
              |
              v
          events.json
```

The architecture aims to keep business logic independent of the user interface and persistence implementation.

This makes it easier to test individual components and eventually introduce additional interfaces without duplicating core functionality.

---

## Development Status

### Implemented

- [x] Basic event management.
- [x] Event display and searching.
- [x] Case-insensitive event lookup.
- [x] Event creation.
- [x] Duplicate event prevention.
- [x] JSON-based persistent storage.
- [x] Object-oriented event representation.
- [x] Event serialization and deserialization.
- [x] Input and state validation.
- [x] Event registration.
- [x] Registration cancellation.
- [x] Registration persistence.
- [x] Missing-file handling.
- [x] Malformed JSON handling.
- [x] Invalid JSON structure handling.
- [x] Individual invalid-record handling.
- [x] Modular application architecture.
- [x] Reusable event-management services.
- [x] Event location editing.
- [x] Event capacity editing.
- [x] Safe event deletion.
- [x] Category filtering.
- [x] Chronological event sorting.
- [x] Automated unit testing.
- [x] CLI testing with mocking.

### Next Development Priorities

- [ ] Improve date validation and handling.
- [ ] Introduce additional event-management capabilities.
- [ ] Improve project organization as complexity increases.
- [ ] Expand automated test coverage.
- [ ] Introduce a more accessible user interface.
- [ ] Explore backend and database integration.

---

## Project Vision

The long-term goal is to evolve CampusPulse into a cross-college event discovery and management platform.

Planned capabilities include:

### For Students
- Student accounts.
- College email verification.
- College profiles.
- Cross-college event discovery.
- Advanced event search and filtering.
- Event registration.
- Personalized event recommendations.

### For Organizers
- Verified student organization accounts.
- Organizer profiles.
- Event creation and management.
- Registration management.
- Event visibility and discovery controls.

### Platform Development
- Web-based interface.
- Backend API.
- Database integration.
- Authentication and authorization.
- Scalable event discovery infrastructure.
- Open-source community contributions.

> **Note:** These are long-term plans and are not part of the current Python CLI prototype.

---

## Contributing

CampusPulse is intended to become an open-source community-driven project.

Development is currently focused on establishing a reliable core application. Contribution guidelines and additional project documentation will evolve as the project matures.

Bug reports, feature suggestions, improvements, and pull requests are welcome.

---

## Development Philosophy

CampusPulse is being developed incrementally, with an emphasis on learning and applying sound software engineering principles.

The guiding principles are:

- Understand the code being written.
- Prioritize functionality over unnecessary complexity.
- Introduce technologies when they solve actual problems.
- Test existing behavior before introducing changes.
- Maintain data integrity.
- Separate application responsibilities.
- Learn from bugs rather than simply suppressing errors.
- Build toward a maintainable and genuinely useful product.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Maintainer

**Darsh Agarwal**

GitHub: [@Zendar6208](https://github.com/Zendar6208)

CampusPulse — Making campus opportunities easier to discover.