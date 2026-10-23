import unittest
from unittest.mock import patch
from main import add_event, main
from event import Event

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

    def test_main_saves_after_successful_creation(self):
        events = []

        with patch("main.load_events", return_value=events), \
            patch("builtins.input", side_effect=[
                "3",
                "Campus Hackathon",
                "Technology",
                "25-10-2026",
                "VIT-AP",
                "100",
                "6"
            ]), \
            patch("main.save_events") as mock_save:

            main()

        mock_save.assert_called_once_with(events)
        self.assertEqual(len(events), 1)

    def test_main_does_not_save_invalid_event(self):
        events = []

        with patch("main.load_events", return_value=events):
            with patch("builtins.input", side_effect=[
                "3",
                "Campus Hackathon",
                "Technology",
                "25-10-2026",
                "VIT-AP",
                "abc",
                "6"
            ]):
                with patch("main.save_events") as mock_save:
                    main()

        mock_save.assert_not_called()
        self.assertEqual(len(events), 0)

    def test_main_saves_after_successful_registration(self):
        events = [
            Event(
                "Campus Hackathon",
                "Technology",
                "25-10-2026",
                "VIT-AP",
                100,
                0
            )
        ]

        with patch("main.load_events", return_value=events): 
            with patch("builtins.input", side_effect=[
                "4",
                "Campus Hackathon",
                "6"
            ]):
                with patch("main.save_events") as mock_save:
                    main()

        mock_save.assert_called_once_with(events)
        self.assertEqual(events[0].registered, 1)

    def test_main_does_not_save_failed_registration(self):
        events = [
                Event(
                "Campus Hackathon",
                "Technology",
                "25-10-2026",
                "VIT-AP",
                100,
                100
            )
        ]
        with patch("main.load_events",return_value=events):
            with patch("builtins.input", side_effect=[
            "4",
            "Campus Hackathon",
            "6"
        ]):
                with patch("main.save_events") as mock_save:
                    main()

        mock_save.assert_not_called()
        self.assertEqual(events[0].registered,100)

        def test_main_saves_after_successful_cancellation(self):
            events = [
                    Event(
                    "Campus Hackathon",
                    "Technology",
                    "25-10-2026",
                    "VIT-AP",
                    100,
                    100
                )
            ]
            with patch("main.load_events",return_value=events):
                with patch("builtins.input", side_effect=[
                "5",
                "Campus Hackathon",
                "6"
            ]):
                    with patch("main.save_events") as mock_save:
                        main()
           
            mock_save.assert_called_once_with(events)
            self.assertEqual(events[0].registered, 4)

        
        
    


    
            
    





    

    