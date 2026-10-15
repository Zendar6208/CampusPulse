import unittest
from main import Event

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
    