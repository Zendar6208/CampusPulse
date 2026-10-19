import unittest
from event import Event
from event_service import find_event_by_name
from event_service import find_event_by_name, create_event

class TestEventService(unittest.TestCase):
    def setUp(self):
        self.events = [
            Event("Hackathon 1", "Technology", "01-01-2023", "Location 1", 100, 0),
            Event("Hackathon 2", "Design", "02-01-2023", "Location 2", 150, 0),
            Event("Hackathon 3", "Marketing", "03-01-2023", "Location 3", 200, 0)
        ]

    def test_find_event_by_name_found(self):
        event = find_event_by_name(self.events, "Hackathon 1")
        self.assertEqual(event.name, "Hackathon 1")

    def test_find_event_by_name_not_found(self):
        event = find_event_by_name(self.events, "Hackathon 4")
        self.assertIsNone(event)

    def test_find_event_by_name_case_insensitive(self):
        event = find_event_by_name(self.events, "HACKATHON 1")
        self.assertIs(event, self.events[0])
    def test_find_event_by_name_empty_string(self):
        event = find_event_by_name(self.events, "")
        self.assertIsNone(event)
    def test_find_event_by_name_whitespace_string(self):
        event = find_event_by_name(self.events, "   ")
        self.assertIsNone(event)
    def test_create_event_success(self):
        new_event= create_event(self.events, "Hackathon 4", "AI", "04-01-2023", "Location 4", 250)
        self.assertEqual(new_event.name, "Hackathon 4")
        self.assertIs(new_event, self.events[-1])
        self.assertEqual(len(self.events), 4)
        self.assertEqual(new_event.registered, 0)
    def test_create_event_negative_capacity(self):
        original_length = len(self.events)
        with self.assertRaises(ValueError):
            create_event(self.events, "Hackathon 5", "AI", "05-01-2023", "Location 5", -10)
        self.assertEqual(len(self.events), original_length)


