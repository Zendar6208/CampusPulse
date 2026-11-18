import unittest
from unittest.mock import patch
from main import add_event,main
from event import Event
from main import filter_events_by_date_range

class TestAddEvent(unittest.TestCase):

    def test_add_event_success(self):
        events = []
        with patch("builtins.input", side_effect=[
            "Campus Hackathon",
            "Technology",
            "25-10-2026",
            "VIT-AP",
            "100"
        ]):
            result = add_event(events)

        self.assertTrue(result)
        self.assertEqual(len(events), 1)
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
                    "10"
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
                "10"
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
                "10"
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

        with patch("main.load_events", return_value=events):
            with patch("builtins.input", side_effect=[
                "4",
                "Campus Hackathon",
                "10"
            ]):
                with patch("main.save_events") as mock_save:
                    main()

        mock_save.assert_not_called()
        self.assertEqual(events[0].registered, 100)

    def test_main_saves_after_successful_cancellation(self):
        events = [
            Event(
                "Campus Hackathon",
                "Technology",
                "25-10-2026",
                "VIT-AP",
                100,
                5
            )
        ]

        with patch("main.load_events", return_value=events):
            with patch("builtins.input", side_effect=[
                "5",
                "Campus Hackathon",
                "10"
            ]):
                with patch("main.save_events") as mock_save:
                    main()

        mock_save.assert_called_once_with(events)
        self.assertEqual(events[0].registered, 4)

    def test_main_does_not_save_failed_cancellation(self):
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
                "5",
                "Campus Hackathon",
                "10"
            ]):
                with patch("main.save_events") as mock_save:
                    main()

        mock_save.assert_not_called()
        self.assertEqual(events[0].registered, 0)

    def test_main_does_not_save_duplicate_event(self):
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

        with patch("main.load_events", return_value=events), \
                patch("builtins.input", side_effect=[
                    "3",
                    "Campus Hackathon",
                    "Technology",
                    "25-10-2026",
                    "VIT-AP",
                    "100",
                    "10"
                ]), \
                patch("main.save_events") as mock_save:

            main()

        mock_save.assert_not_called()
        self.assertEqual(len(events), 1)

    def test_main_saves_successful_location_update(self):
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

        with patch("main.load_events", return_value=events), \
                patch("builtins.input", side_effect=[
                    "6",
                    "Campus Hackathon",
                    "Main Auditorium",
                    "10"
                ]), \
                patch("main.save_events") as mock_save:

            main()

        self.assertEqual(events[0].location, "Main Auditorium")
        mock_save.assert_called_once_with(events)

    def test_main_does_not_save_location_update_when_event_missing(self):
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

        with patch("main.load_events", return_value=events), \
                patch("builtins.input", side_effect=[
                    "6",
                    "Unknown Hackathon",
                    "Main Auditorium",
                    "10"
                ]), \
                patch("main.save_events") as mock_save:

            main()

        self.assertEqual(events[0].location, "VIT-AP")
        mock_save.assert_not_called()

    def test_main_does_not_save_empty_location_update(self):
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

        with patch("main.load_events", return_value=events), \
                patch("builtins.input", side_effect=[
                    "6",
                    "Campus Hackathon",
                    " ",
                    "10"
                ]), \
                patch("main.save_events") as mock_save:

            main()

        self.assertEqual(events[0].location, "VIT-AP")
        mock_save.assert_not_called()

    def test_main_saves_successful_capacity_update(self):
        events = [
            Event(
                "Campus Hackathon",
                "Technology",
                "25-10-2026",
                "VIT-AP",
                100,
                25
            )
        ]

        with patch("main.load_events", return_value=events), \
                patch("builtins.input", side_effect=[
                    "7",
                    "Campus Hackathon",
                    "150",
                    "10"
                ]), \
                patch("main.save_events") as mock_save:

            main()

        self.assertEqual(events[0].capacity, 150)
        self.assertEqual(events[0].registered, 25)
        mock_save.assert_called_once_with(events)

    def test_main_does_not_save_capacity_below_registrations(self):
        events = [
            Event(
                "Campus Hackathon",
                "Technology",
                "25-10-2026",
                "VIT-AP",
                100,
                25
            )
        ]

        with patch("main.load_events", return_value=events), \
                patch("builtins.input", side_effect=[
                    "7",
                    "Campus Hackathon",
                    "20",
                    "10"
                ]), \
                patch("main.save_events") as mock_save:

            main()

        self.assertEqual(events[0].capacity, 100)
        self.assertEqual(events[0].registered, 25)
        mock_save.assert_not_called()

    def test_main_does_not_save_invalid_capacity_input(self):
        events = [
            Event(
                "Campus Hackathon",
                "Technology",
                "25-10-2026",
                "VIT-AP",
                100,
                25
            )
        ]

        with patch("main.load_events", return_value=events), \
                patch("builtins.input", side_effect=[
                    "7",
                    "Campus Hackathon",
                    "invalid",
                    "10"
                ]), \
                patch("main.save_events") as mock_save:

            main()

        self.assertEqual(events[0].capacity, 100)
        self.assertEqual(events[0].registered, 25)
        mock_save.assert_not_called()

    def test_main_saves_successful_event_deletion(self):
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

        with patch("main.load_events", return_value=events), \
                patch("builtins.input", side_effect=[
                    "8",
                    "Campus Hackathon",
                    "10"
                ]), \
                patch("main.save_events") as mock_save:

            main()

        self.assertEqual(len(events), 0)
        mock_save.assert_called_once_with(events)

    def test_main_does_not_save_event_with_active_registrations(self):
        events = [
            Event(
                "Campus Hackathon",
                "Technology",
                "25-10-2026",
                "VIT-AP",
                100,
                25
            )
        ]

        with patch("main.load_events", return_value=events):
            with patch("builtins.input", side_effect=[
                "8",
                "Campus Hackathon",
                "10"
            ]):
                with patch("main.save_events") as mock_save:
                    main()

        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].registered, 25)
        mock_save.assert_not_called()

    def test_main_does_not_save_when_deleting_nonexistent_event(self):
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

        with patch("main.load_events", return_value=events), \
                patch("builtins.input", side_effect=[
                    "8",
                    "Nonexistent Event",
                    "10"
                ]), \
                patch("main.save_events") as mock_save:

            main()

        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].name, "Campus Hackathon")
        mock_save.assert_not_called()

    def test_main_filters_events_by_category(self):
        events = [
            Event("Campus Hackathon", "Technology", "25-10-2026", "VIT-AP", 100, 0),
            Event("Art Exhibition", "Arts", "15-11-2026", "VIT-AP", 50, 0),
            Event("Coding Bootcamp", "Technology", "05-12-2026", "VIT-AP", 80, 0)
        ]

        with patch("main.load_events", return_value=events), \
                patch("builtins.input", side_effect=["9", "Technology", "10"]), \
                patch("main.save_events") as mock_save, \
                patch("builtins.print") as mock_print:

            main()

        printed_output = "\n".join(
            str(arg)
            for call in mock_print.call_args_list
            for arg in call.args
        )

        self.assertIn("Campus Hackathon", printed_output)
        self.assertIn("Coding Bootcamp", printed_output)
        self.assertNotIn("Art Exhibition", printed_output)

        # Filtering events should not trigger a save operation
        mock_save.assert_not_called()

    def test_filter_events_by_date_range_displays_matching_events(self):
        events = [
            Event("Campus Hackathon", "Technology", "25-10-2026", "VIT-AP", 100, 0),
            Event("Art Exhibition", "Arts", "15-11-2026", "VIT-AP", 50, 0),
            Event("Coding Bootcamp", "Technology", "05-12-2026", "VIT-AP", 80, 0)
        ]

        start_date = "01-11-2026"
        end_date = "30-11-2026"

        with patch("builtins.input", side_effect=[start_date, end_date]), \
                patch("builtins.print") as mock_print:

            filter_events_by_date_range(events)

        printed_output = "\n".join(
            str(arg)
            for call in mock_print.call_args_list
            for arg in call.args
        )

        self.assertIn("Art Exhibition", printed_output)
        self.assertNotIn("Campus Hackathon", printed_output)
        self.assertNotIn("Coding Bootcamp", printed_output)

    def test_filter_events_by_date_range_handles_invalid_dates(self):
        events = []
        start_date = "invalid-date"
        end_date = "30-11-2026"
        with patch("builtins.input", side_effect=[start_date, end_date]), \
                patch("builtins.print") as mock_print:
            filter_events_by_date_range(events)

            mock_print.assert_called_once()
            self.assertIn("Unable to filter events", mock_print.call_args.args[0])

    def test_filter_events_by_date_range_displays_message_when_no_events_match(self):
        events = [
            Event("Campus Hackathon", "Technology", "25-10-2026", "VIT-AP", 100, 0),
            Event("Art Exhibition", "Arts", "05-12-2026", "VIT-AP", 50, 0)
        ]
        start_date = "01-11-2026"
        end_date = "30-11-2026"

        with patch("builtins.input", side_effect=[start_date, end_date]), \
                patch("builtins.print") as mock_print:

            filter_events_by_date_range(events)

        mock_print.assert_called_once()
        self.assertIn(f"No events found between {start_date} and {end_date}.", mock_print.call_args.args[0])

    def test_main_calls_date_range_filtering(self):
        events = [
            Event("Campus Hackathon", "Technology", "25-10-2026", "VIT-AP", 100, 0),
            Event("Art Exhibition", "Arts", "15-11-2026", "VIT-AP", 50, 0)
        ]
        

        with patch("main.load_events", return_value=events), \
                patch("main.filter_events_by_date_range") as mock_filter, \
                patch("builtins.input", side_effect=["10","11"]), \
                patch("builtins.print") as mock_print:

            main()

        mock_filter.assert_called_once_with(events)

if __name__ == "__main__":
    unittest.main()