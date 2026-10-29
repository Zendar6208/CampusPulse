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

### Automated Testing

* Unit tests using Python's built-in `unittest` framework.
* Registration and cancellation tests.
* Event capacity detection tests.
* Constructor validation tests.
* Nine automated test cases implemented.

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
* Python `unittest` for automated testing
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
python main.py
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
├── main.py
├── test_event.py
├── events.json
├── README.md
├── LICENSE
└── .gitignore
```

The structure will evolve as the project grows.

## Running Tests

CampusPulse uses Python's built-in `unittest` framework.

Run the automated tests using:

```bash
python -m unittest test_event -v
```

The test suite currently contains nine tests covering registration, cancellation, capacity detection, and input validation.

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
* [x] Automated unit testing
* [x] Constructor validation tests

### Next Development Priorities

* [ ] Automated testing for JSON persistence
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

### Day 10 — Testing Input Validation

Expanded the automated test suite to verify that CampusPulse correctly rejects invalid event data.

**What I implemented:**

* Learned to use `assertRaises()` from Python's `unittest` framework.
* Added three constructor validation tests:

  * Reject negative event capacity.
  * Reject registration counts exceeding event capacity.
  * Reject negative registration counts.
* Tested invalid inputs during object creation rather than modifying existing objects.
* Expanded the test suite from six to nine tests.

**Key learning:** Testing isn't only about confirming that valid operations succeed. It's equally important to verify that invalid operations fail in the expected way.

### Day 11 — Automated Persistence Testing

**Objective:** Expand automated testing beyond individual `Event` methods to verify JSON persistence and failure handling.

**What I implemented:**

* Added automated tests for event serialization using `to_dict()`.
* Added deserialization tests using `Event.from_dict()`.
* Refactored `save_events()` and `load_events()` to accept optional file paths while preserving `events.json` as the default.
* Used `tempfile.TemporaryDirectory()` to test file operations without modifying actual application data.
* Implemented round-trip persistence testing with multiple events.
* Tested loading behaviour when a JSON file is missing or malformed.
* Tested preservation of valid events when an invalid record appears between them.
* Identified and fixed an unhandled `KeyError` caused by missing required event fields.
* Added a test verifying that invalid JSON root structures are rejected.
* Expanded the automated test suite toward 16 test cases.

**Key learning:** Automated tests should verify not only successful operations but also how software behaves when files are missing, data is corrupted, or individual records are invalid.

### Day 12 — Modular Architecture & Search Testing

**Objective:** Improve project maintainability by separating responsibilities into independent Python modules.

**What I implemented:**

* Extracted the `Event` class into `event.py`.
* Moved JSON persistence functions into `storage.py`.
* Extracted reusable event lookup logic into `event_service.py`.
* Refactored `main.py` to focus on CLI interactions and application flow.
* Updated test imports to reference their respective modules directly.
* Introduced `test_event_service.py` for testing event lookup independently.
* Added automated tests covering:

  * Successful event lookup.
  * Missing events.
  * Case-insensitive searching.
  * Empty search strings.
  * Whitespace-only search strings.
* Expanded the automated test suite to 21 tests.

**Key learning:** Separating responsibilities makes code easier to understand, maintain, test and reuse. Application logic should remain independent of the interface through which users interact with it.

### Day 13 — Reusable Event Creation & Automated Testing

**Objective:** Separate event creation logic from CLI interactions to improve modularity and prepare CampusPulse for future interfaces.

**Implemented:**

* Introduced `create_event()` in `event_service.py`.
* Separated event creation from terminal input handling.
* Refactored `add_event()` to use the event creation service.
* Preserved existing event validation through the `Event` constructor.
* Ensured invalid events are rejected before modifying the event collection.
* Added automated tests for successful event creation, negative capacity, invalid event collection types, and invalid input types.
* Expanded the automated test suite to 25 tests.

**Key Learning:**

Separating application logic from user-interface code allows the same functionality to be reused across different interfaces without duplicating implementation.

### Day 14 — Registration & Cancellation Service Refactoring

**Objective:** Separate registration management from CLI interactions and improve the testability of event operations.

**What I implemented:**

* Introduced `register_for_event()` in `event_service.py`.
* Introduced `cancel_event_registration()` as a reusable service function.
* Reused `find_event_by_name()` for locating events.
* Delegated registration and cancellation rules to the existing `Event` class methods.
* Added input type validation to both service functions.
* Refactored the CLI to use the registration and cancellation services.
* Fixed an issue where cancellation could execute twice for a single request.
* Ensured event data is saved only after successful registration or cancellation.
* Added automated tests covering:

  * Successful registration and cancellation.
  * Nonexistent events.
  * Full-capacity registration attempts.
  * Cancellation attempts with zero registrations.
  * Invalid event collection types.
  * Invalid event name types.
* Expanded the automated test suite from 25 to 35 tests.

**Key Learning:**

Separating business logic from user-interface code prevents duplicated operations and makes application behaviour easier to test. Reusing existing class methods also ensures that registration rules remain consistent throughout the application.

### Day 15 — Improving Event Creation and Persistence

**Objective:** Ensure event data is saved only after successful event creation and introduce automated testing for CLI input handling.

**What I implemented:**

* Updated `add_event()` to return `True` after successful creation and `False` when input validation fails.
* Modified the CLI to call `save_events()` only when `add_event()` succeeds.
* Introduced `test_main.py` to test CLI functions independently.
* Used `unittest.mock.patch` to simulate user input without manual interaction.
* Added five tests covering:

  * Successful event creation.
  * Empty event names.
  * Non-integer capacity.
  * Negative capacity.
  * Invalid events collection type.
* Expanded the automated test suite to 36 tests.

**Key Learning:**

Functions can communicate operation outcomes through return values. Separating successful and unsuccessful execution paths helps prevent unnecessary file operations and makes CLI behaviour easier to verify through automated tests.
### Day 16 — Testing CLI Persistence with Mocking

**Objective:** Verify that CampusPulse saves event data only after successful operations.

**What I implemented:**

* Introduced CLI-level persistence tests using `unittest.mock.patch`.
* Mocked `load_events()` to provide controlled test data.
* Mocked `input()` to simulate complete CLI interactions.
* Mocked `save_events()` to verify persistence without modifying `events.json`.
* Added tests covering:

  * Successful event creation triggers saving exactly once.
  * Invalid event creation does not trigger saving.
  * Successful registration triggers saving exactly once.
  * Failed registration does not trigger saving.
  * Successful cancellation triggers saving exactly once.
  * Failed cancellation does not trigger saving.
* Added assertions to verify that registration counts change by exactly one.
* Expanded the automated test suite to 42 tests.

**Key Learning:**

Mocking allows us to test how different parts of an application interact without depending on actual keyboard input or file operations. Testing both successful and failed operations helps prevent unnecessary persistence and catches bugs that isolated function tests might miss.

### Day 17 — Duplicate Event Prevention

* Implemented duplicate event-name detection in the service layer.
* Used case-insensitive matching to prevent duplicates with different capitalization.
* Normalized event names by removing leading and trailing whitespace.
* Added unit tests for exact duplicates, case-insensitive duplicates, and whitespace-based duplicates.
* Verified that newly created event names are stored without surrounding whitespace.
* Added a mocked CLI test ensuring duplicate event attempts do not trigger `save_events()`.

**Key learning:** Input normalization, data integrity, and testing persistence behaviour across application layers.

### Day 18 — Event Location Editing

* Implemented `update_event()` in the service layer to modify an existing event's location.
* Added input validation to reject invalid types and empty or whitespace-only locations.
* Normalized location input using `.strip()`.
* Preserved existing event registrations when updating the location.
* Integrated event editing into the CLI through menu option 7.
* Ensured that changes are saved only after a successful update.
* Added service-layer and mocked CLI tests covering successful updates, missing events, invalid inputs, and persistence behaviour.

**Key learning:** Updating existing objects safely, separating business logic from CLI interaction, and preventing unsuccessful operations from triggering persistence.

### Day 19 — Event Capacity Editing

* Implemented `update_event_capacity()` in the service layer.
* Added validation for invalid types, negative capacities, and capacities below existing registrations.
* Prevented Boolean values from being accepted as integers.
* Preserved existing registrations during capacity updates.
* Added unit tests covering successful updates, boundary conditions, invalid inputs, and missing events.
* Integrated capacity editing into the CLI through menu option 8.
* Ensured that `save_events()` runs only after a successful update.
* Added mocked CLI tests covering successful persistence, rejected capacity reductions, and nonnumeric input.

**Key learning:** Enforcing business rules before modifying data, testing boundary conditions, and maintaining data integrity across the service and CLI layers.

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
