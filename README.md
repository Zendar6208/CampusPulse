# CampusPulse

CampusPulse is an open-source platform designed to help college students discover hackathons, competitions, workshops, fests, conferences, and other college events in one place.

The long-term goal is to create a trusted campus event network where students can discover opportunities and verified college clubs and organisers can publish and manage their events.

> **Status:** Early development / Python prototype

## Why CampusPulse?

College students often discover events through scattered sources such as Instagram, WhatsApp groups, Telegram channels, college websites, and individual event pages.

CampusPulse brings event opportunities together in one platform and builds a system for verified college organisations and organisers.

## Current Goal

Build a working foundation for CampusPulse and gradually evolve it into a full-fledged platform.

I'm developing the project incrementally alongside my software engineering learning, with each stage introducing new concepts and improving the existing system.

## Current Features

The current prototype is a Python-based event management system that supports:

* Displaying upcoming events
* Searching for events by name
* Case-insensitive event search
* Adding new events
* Viewing event information
* Managing event capacity and registration counts
* Registering participants for events
* Detecting when an event is full
* Command-line menu navigation
* Basic input validation
* Robust handling of missing `events.json`
* Handling of corrupted/invalid JSON data
* Event data type validation
* Empty event-state handling
* Object-oriented event representation
* Converting event objects to dictionaries for JSON storage
* Reconstructing event objects from stored JSON data

## Current Data

Events currently contain:

* Event name
* Category
* Date
* Location
* Capacity
* Number of registered participants

## Current Technology

The project currently uses:

* Python
* Lists
* Dictionaries
* Classes and objects
* Instance attributes
* Instance methods
* Class methods
* Functions
* Loops
* Conditional statements
* String manipulation
* Input validation
* Git & GitHub
* JSON file persistence
* Object serialization and deserialization
* Exception handling
* `try/except`
* `FileNotFoundError`
* `JSONDecodeError`
* `TypeError`

As development progresses, the project will gradually evolve into a full-stack application.

## Project Vision

The planned direction for CampusPulse includes:

* Student accounts
* College email verification
* College profiles
* Verified student organizations
* Organizer accounts
* Event creation and management
* Event registration
* Event search and filtering
* Cross-college event discovery
* Personalized event recommendations
* Open-source contributions from students and developers

These features are part of the project's direction and are **not yet implemented**.

## Getting Started

### Requirements

* Python 3.x
* Git

### Run the current prototype

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd CampusPulse
```

Run the program:

```bash
python main
```

## Project Structure

```text
CampusPulse/
│
├── main
├── main.py
├── events.json
├── README.md
├── LICENSE
└── .gitignore
```

The project structure will evolve as CampusPulse grows.

## Contributing

CampusPulse is intended to become an open-source project.

At the current stage, development is primarily focused on building and testing the core functionality. Contribution guidelines will be added as the project becomes ready for external contributors.

If you have an idea, find a bug, or want to contribute, feel free to open an issue or submit a pull request.

## Development Philosophy

CampusPulse is being built incrementally.

The project will evolve alongside the developer's technical knowledge, starting with a simple Python prototype and gradually introducing more advanced concepts and technologies when they are needed.

The goal is to build a substantial, working software project rather than a collection of disconnected features.

## 📊 Development Status

CampusPulse is currently in active early development.

### Implemented

* [x] JSON-based event storage
* [x] Load events when the application starts
* [x] Save newly added events to persistent storage
* [x] Basic event management system
* [x] Display events
* [x] Search events
* [x] Case-insensitive event search
* [x] Add new events
* [x] Input validation
* [x] Basic error handling for missing and corrupted event data
* [x] Event data validation
* [x] Introduced an `Event` class
* [x] Learned and implemented object-oriented concepts
* [x] Added instance attributes and methods to the `Event` class
* [x] Added `to_dict()` for event serialization
* [x] Added `from_dict()` for event deserialization
* [x] Converted loaded event dictionaries into `Event` objects
* [x] Converted newly added events into `Event` objects
* [x] Added event registration behavior
* [x] Added event capacity checking with `is_full()`
* [x] Persisted updated registration counts to JSON

## 📝 Development Log

### Day 1 — Initial Prototype

* Created the first Python-based CampusPulse event management system.
* Implemented event display, search, and event creation.
* Added basic input validation.
* Added case-insensitive event searching.

### Day 2 — Persistent Event Storage

* Introduced JSON-based data storage.
* Added `load_events()` to load event data when the application starts.
* Added `save_events()` to persist changes to `events.json`.
* Connected event creation to persistent storage.
* Tested that newly added events remain available after restarting the application.

### Day 3 — Error Handling & Data Validation

* Added error handling for a missing `events.json` file using `FileNotFoundError`.
* Added error handling for corrupted or invalid JSON data using `json.JSONDecodeError`.
* Added validation to ensure event data is stored as a list.
* Added handling for empty event lists when displaying events.
* Practiced Python exception handling using specific exceptions instead of broad exception handling.
* Improved the reliability of the event data loading and display process.

### Day 4 — Introduction to Object-Oriented Programming

* Introduced the `Event` class to represent individual campus events.
* Learned the difference between classes and objects.
* Learned how `self` refers to the current object instance.
* Used `__init__()` to initialize event attributes.
* Added instance attributes for event name, category, date, location, capacity, and registration count.
* Added an instance method to display event information.
* Began transitioning the project from dictionary-based event representation toward an object-oriented data model.

### Day 5 — OOP Integration & Event Behavior

* Converted JSON event dictionaries into `Event` objects when loading data.
* Added `to_dict()` to convert `Event` objects back into dictionaries for JSON storage.
* Added `from_dict()` as a class method for reconstructing `Event` objects from dictionaries.
* Refactored `display_events()` to use the `Event.display()` method.
* Refactored `search_event()` to work with object attributes and methods.
* Updated `add_event()` to create `Event` objects instead of dictionaries.
* Added the `register()` method to handle event registration.
* Added the `is_full()` method to centralize event capacity checking.
* Connected registration changes to persistent JSON storage.
* Tested the complete object-to-JSON and JSON-to-object workflow.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Maintainer

**Darsh Agarwal**

CampusPulse is an open-source project built as a learning project with the goal of eventually becoming a useful platform for college students.
