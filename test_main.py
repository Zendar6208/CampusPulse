import unittest
from unittest.mock import patch
from main import add_event

class TestAddEvent(unittest.TestCase):

    def test_add_event_success(self):
        events=[]
        with patch("builtins.input", side_effect=[
        "Campus Hackathon",
        "Technology",
        "25-10-2026",
        "VIT-AP",
        "100"
        ]):
            result=add_event(events)
        self.assertTrue(result)
        self.assertEqual(len(events),1)
        self.assertEqual(events[0].name, "Campus Hackathon")


    def test_add_event_empty_name(self):
        events = []

        with patch("builtins.input", side_effect=[
            "",
            "Technology",
            "25-10-2026",
            "VIT-AP",
            "100"
        ]):
            result = add_event(events)

        self.assertFalse(result)
        self.assertEqual(len(events), 0)


    def test_add_event_invalid_capacity(self):
        events = []
        
        with patch("builtins.input", side_effect=[
            "Hackathon",
            "Technology",
            "25-10-2026",
            "VIT-AP",
            "abc"
        ]):
            result = add_event(events)
        
        self.assertFalse(result)
        self.assertEqual(len(events), 0)


    def test_add_event_negative_capacity(self):
        events = []

        with patch("builtins.input", side_effect=[
            "Hackathon",
            "Technology",
            "25-10-2026",
            "VIT-AP",
            "-5"
        ]):
            result = add_event(events)

        self.assertFalse(result)
        self.assertEqual(len(events), 0)


    def test_add_event_invalid_events_type(self):
        with self.assertRaises(TypeError):
            add_event("not a list")

           
    





    

    