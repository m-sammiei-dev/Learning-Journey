import unittest
from time_calculator import add_time


class TestAddTime(unittest.TestCase):

    # -----------------------------
    # happy path / basic behavior
    # -----------------------------
    def test_simple_addition(self):
        result = add_time("3:00 PM", "3:10")
        self.assertEqual(result["result"], "6:10 PM")

    def test_next_day(self):
        result = add_time("11:30 PM", "2:32")
        self.assertEqual(result["result"], "2:02 AM (next day)")

    def test_with_day_of_week(self):
        result = add_time("11:43 PM", "24:20", "Tuesday")
        self.assertEqual(result["result"], "12:03 AM, Thursday (2 days later)")

    def test_many_days_later(self):
        result = add_time("8:16 PM", "466:02", "tuesday")
        self.assertEqual(result["result"], "6:18 AM, Monday (20 days later)")

    # -----------------------------
    # boundary around noon/midnight
    # -----------------------------
    def test_noon_stays_pm(self):
        result = add_time("11:59 AM", "0:01")
        self.assertEqual(result["result"], "12:00 PM")

    def test_midnight_transition(self):
        result = add_time("11:59 PM", "0:01")
        self.assertEqual(result["result"], "12:00 AM (next day)")

    def test_exactly_12_hours_pm_to_am(self):
        result = add_time("6:00 PM", "12:00")
        self.assertEqual(result["result"], "6:00 AM (next day)")

    def test_exactly_12_hours_am_to_pm(self):
        result = add_time("6:00 AM", "12:00")
        self.assertEqual(result["result"], "6:00 PM")

    def test_exactly_24_hours(self):
        result = add_time("3:15 PM", "24:00")
        self.assertEqual(result["result"], "3:15 PM (next day)")

    # -----------------------------
    # minute overflow cases
    # -----------------------------
    def test_minute_overflow_small(self):
        result = add_time("5:50 PM", "0:15")
        self.assertEqual(result["result"], "6:05 PM")

    def test_minute_overflow_to_next_day(self):
        result = add_time("11:50 PM", "0:15")
        self.assertEqual(result["result"], "12:05 AM (next day)")

    def test_zero_duration(self):
        result = add_time("4:40 PM", "0:00")
        self.assertEqual(result["result"], "4:40 PM")

    # -----------------------------
    # multiple day transitions
    # -----------------------------
    def test_two_days_later(self):
        result = add_time("1:00 AM", "48:00")
        self.assertEqual(result["result"], "1:00 AM (2 days later)")

    def test_one_day_with_weekday(self):
        result = add_time("9:13 PM", "24:00", "Sunday")
        self.assertEqual(result["result"], "9:13 PM, Monday (next day)")

    def test_three_days_later_with_weekday(self):
        result = add_time("10:10 PM", "72:00", "Friday")
        self.assertEqual(result["result"], "10:10 PM, Monday (3 days later)")

    # -----------------------------
    # weekday normalization
    # -----------------------------
    def test_weekday_lowercase_input(self):
        result = add_time("2:59 AM", "24:00", "monday")
        self.assertEqual(result["result"], "2:59 AM, Tuesday (next day)")

    def test_weekday_uppercase_input(self):
        result = add_time("2:59 AM", "24:00", "MONDAY")
        self.assertEqual(result["result"], "2:59 AM, Tuesday (next day)")

    def test_weekday_mixed_case_input(self):
        result = add_time("2:59 AM", "24:00", "MoNdAy")
        self.assertEqual(result["result"], "2:59 AM, Tuesday (next day)")

    # -----------------------------
    # large duration stress tests
    # -----------------------------
    def test_large_duration_whole_days(self):
        result = add_time("12:00 PM", "240:00")
        self.assertEqual(result["result"], "12:00 PM (10 days later)")

    def test_large_duration_with_weekday(self):
        result = add_time("12:00 PM", "240:00", "Wednesday")
        self.assertEqual(result["result"], "12:00 PM, Saturday (10 days later)")

    def test_very_large_duration(self):
        result = add_time("1:01 AM", "1000:59", "Sunday")
        self.assertEqual(result["result"], "6:00 PM, Saturday (41 days later)")

    # -----------------------------
    # format correctness checks
    # -----------------------------
    def test_result_has_result_key(self):
        result = add_time("3:00 PM", "3:10")
        self.assertIn("result", result)

    def test_result_is_dict(self):
        result = add_time("3:00 PM", "3:10")
        self.assertIsInstance(result, dict)

    def test_no_day_in_output_when_day_not_provided(self):
        result = add_time("3:00 PM", "3:10")
        self.assertNotIn(",", result["result"])

    # -----------------------------
    # invalid input types
    # -----------------------------
    def test_invalid_start_type_int(self):
        with self.assertRaises(TypeError):
            add_time(300, "3:10")

    def test_invalid_duration_type_int(self):
        with self.assertRaises(TypeError):
            add_time("3:00 PM", 310)

    def test_invalid_day_type_int(self):
        with self.assertRaises(TypeError):
            add_time("3:00 PM", "3:10", 5)

    # -----------------------------
    # invalid input values
    # these assume your function validates content,
    # not just type. if not implemented yet, these may fail.
    # -----------------------------
    def test_invalid_start_missing_am_pm(self):
        with self.assertRaises(ValueError):
            add_time("3:00", "3:10")

    def test_invalid_start_bad_hour(self):
        with self.assertRaises(ValueError):
            add_time("13:00 PM", "1:00")

    def test_invalid_start_bad_minute(self):
        with self.assertRaises(ValueError):
            add_time("3:60 PM", "1:00")

    def test_invalid_duration_bad_format(self):
        with self.assertRaises(ValueError):
            add_time("3:00 PM", "abc")

    def test_invalid_duration_bad_minute(self):
        with self.assertRaises(ValueError):
            add_time("3:00 PM", "5:60")

    def test_invalid_day_name(self):
        with self.assertRaises(ValueError):
            add_time("3:00 PM", "2:10", "Funday")


if __name__ == "__main__":
    unittest.main()
