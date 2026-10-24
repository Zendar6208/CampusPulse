import unittest
from event import Event
from event_service import find_event_by_name, create_event, register_for_event, cancel_event_registration

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

    def test_create_event_invalid_events_type(self):
        with self.assertRaises(TypeError):
            create_event("not a list", "Hackathon 6", "AI", "06-01-2023", "Location 6", 100)

    def test_create_event_invalid_input_types(self):
        with self.assertRaises(TypeError):
            create_event(self.events, 123, "AI", "07-01-2023", "Location 7", 100)
        with self.assertRaises(TypeError):
            create_event(self.events, "Hackathon 7", 456, "07-01-2023", "Location 7", 100)
        with self.assertRaises(TypeError):
            create_event(self.events, "Hackathon 7", "AI", 789, "Location 7", 100)
        with self.assertRaises(TypeError):
            create_event(self.events, "Hackathon 7", "AI", "07-01-2023", 101112, 100)
        with self.assertRaises(TypeError):
            create_event(self.events, "Hackathon 7", "AI", "07-01-2023", "Location 7", "not an int")
            
    def test_register_for_event_success(self):
        event=self.events[0]
        original_registered = event.registered
        event_name="Hackathon 1"
        result = register_for_event(self.events, event_name)
        self.assertTrue(result)
        self.assertEqual(event.registered, original_registered + 1)
    def test_register_for_event_not_found(self):
        event_name = "Nonexistent Event"

        original_counts = [event.registered for event in self.events]

        result = register_for_event(self.events, event_name)
        
        self.assertFalse(result)
        self.assertEqual([event.registered for event in self.events], original_counts)
    
    def test_register_for_event_invalid_events_type(self):
        with self.assertRaises(TypeError):
            register_for_event("not a list", "Hackathon 1")


    def test_register_for_event_invalid_event_name_type(self):
        with self.assertRaises(TypeError):
            register_for_event(self.events, 123)

    def test_register_for_event_full_capacity(self):
        event = self.events[0]
        event.registered = event.capacity

        event_name = event.name

        result = register_for_event(self.events, event_name)

        self.assertFalse(result)
        self.assertEqual(event.registered, event.capacity)


    def test_cancel_registration_for_event_success(self):
        event = self.events[0]
        event.registered = 5

        original_registered = event.registered
        event_name = "Hackathon 1"

        result = cancel_event_registration(self.events, event_name)

        self.assertTrue(result)
        self.assertEqual(event.registered, original_registered - 1)


def test_cancel_registration_for_event_zero_registrations(self):
    event = self.events[0]
    event.registered = 0

    event_name = event.name

    result = cancel_event_registration(self.events, event_name)

    self.assertFalse(result)
    self.assertEqual(event.registered, 0)


    def test_cancel_registration_for_event_not_found(self):
        event_name = "Nonexistent Event"
        original_counts = [event.registered for event in self.events]

        result = cancel_event_registration(self.events, event_name)
                
        self.assertFalse(result)
        self.assertEqual([event.registered for event in self.events], original_counts)

    def test_cancel_registration_invalid_events_type(self):
        with self.assertRaises(TypeError):
            cancel_event_registration("not a list", "Hackathon 1")


    def test_cancel_registration_invalid_event_name_type(self):
        with self.assertRaises(TypeError):
            cancel_event_registration(self.events, 123)

    def test_create_event_duplicate_name(self):
        original_count = len(self.events)
        with self.assertRaises(ValueError):
            create_event(
                self.events,
                "Hackathon 1",
                "AI",
                "04-01-2023",
                "Location 4",
                250,
            )
        self.assertEqual(len(self.events), original_count)

    def test_create_event_duplicate_name_case_insensitive(self):
        original_count=len(self.events)
        with self.assertRaises(ValueError):
            create_event(
                self.events,
                "hAcKaThOn 1",
                "AI",
                "04-01-2023",
               "Location 4",
               250,
            )
        self.assertEqual(len(self.events), original_count)

    



