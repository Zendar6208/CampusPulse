import unittest
from event import Event
from event_service import find_event_by_name

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
        self.assertEqual(event.name, "Hackathon 1")
