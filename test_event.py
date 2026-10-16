import unittest
import tempfile
import os
import json

from main import Event, save_events, load_events

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.event = Event(
            "Test Event",
            "Test Category",
            "2023-10-10",
            "Test Location",
            100,
            50
        )

    def test_register_success(self):
        result = self.event.register()
        self.assertTrue(result)
        self.assertEqual(self.event.registered, 51)
    def test_register_full(self):
        
        self.event.registered = 100

        result = self.event.register()

        self.assertFalse(result)
        self.assertEqual(self.event.registered, 100)
    def test_cancel_success(self):
        result = self.event.cancel_registration()

        self.assertTrue(result)
        self.assertEqual(self.event.registered, 49)
    def test_cancel_empty(self):
        self.event.registered = 0

        result = self.event.cancel_registration()

        self.assertFalse(result)
        self.assertEqual(self.event.registered, 0)
    def test_is_full(self):
        self.event.registered = 100

        result = self.event.is_full()

        self.assertTrue(result)
    def test_is_not_full(self):
        self.event.registered = 50

        result = self.event.is_full()

        self.assertFalse(result)
    def test_negative_capacity(self):
        with self.assertRaises(ValueError):
            Event(
                "Test Event",
                "Hackathon",
                "2026-10-20",
                "VIT-AP",
                -10,
                0
            )
    def test_negative_registered(self):
        with self.assertRaises(ValueError):
            Event(
                "Test Event",
                "Hackathon",
                "2026-10-20",
                "VIT-AP",
                100,
                -5
            )
    def test_registered_exceeds_capacity(self):
        with self.assertRaises(ValueError):
            Event(
                "Test Event",
                "Hackathon",
                "2026-10-20",
                "VIT-AP",
                100,
                150
            )
    def test_to_dict(self):
        expected_dict = {
            "name": "Test Event",
            "category": "Test Category",
            "date": "2023-10-10",
            "location": "Test Location",
            "capacity": 100,
            "registered": 50
        }
        self.assertEqual(self.event.to_dict(), expected_dict)
    def test_from_dict(self):
        event_dict = {
            "name": "Test Event",
            "category": "Test Category",
            "date": "2023-10-10",
            "location": "Test Location",
            "capacity": 100,
            "registered": 50
        }
        event = Event.from_dict(event_dict)
        self.assertIsInstance(event, Event)
        self.assertEqual(event.name, "Test Event")
        self.assertEqual(event.category, "Test Category")
        self.assertEqual(event.date, "2023-10-10")
        self.assertEqual(event.location, "Test Location")
        self.assertEqual(event.capacity, 100)
        self.assertEqual(event.registered, 50)
    def test_save_and_load_events(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = os.path.join(temp_dir, "test_events.json")

            events = [
                Event("Event 1", "Category 1", "2023-10-10", "Location 1", 100, 50),
                Event("Event 2", "Category 2", "2023-11-15", "Location 2", 200, 150)
            ]

            save_events(events, filename=temp_file)

            loaded_events = load_events(filename=temp_file)

            self.assertEqual(len(loaded_events), len(events))
            for original, loaded in zip(events, loaded_events):
                self.assertEqual(original.to_dict(), loaded.to_dict())
    def test_load_missing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file= os.path.join(temp_dir,"non_existent_file.json")
            loaded_events = load_events(filename=temp_file)
            self.assertEqual(loaded_events, [])
    def test_load_malformed_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file=os.path.join(temp_dir,"malformed.json")
            with open(temp_file, "w", encoding="utf-8") as f:
                f.write("{malformed json}")
                f.flush()
            loaded_events = load_events(filename=temp_file)
            self.assertEqual(loaded_events, [])
    def test_load_skips_invalid_event(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = os.path.join(temp_dir, "invalid_event.json")
            invalid_event_data = [
                {
                    "name": "Valid Event",
                    "category": "Category",
                    "date": "2023-10-10",
                    "location": "Location",
                    "capacity": 100,
                    "registered": 50
                },
                {
                    # Missing 'name' field
                    "category": "Category",
                    "date": "2023-11-15",
                    "location": "Location",
                    "capacity": 200,
                    "registered": 150
                },
                {
                    "name": "Second Valid Event",
                    "category": "Workshop",
                    "date": "2023-12-10",
                    "location": "Location 2",
                    "capacity": 200,
                    "registered": 75
                }
    
            ]
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(invalid_event_data, f)
            
            loaded_events = load_events(filename=temp_file)
            self.assertEqual(len(loaded_events), 2)
            self.assertEqual(
            [event.name for event in loaded_events],
            ["Valid Event", "Second Valid Event"]
            )

