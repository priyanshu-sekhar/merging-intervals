from unittest import TestCase
from interval import parse_input, merge_intervals, Interval


class TestInterval(TestCase):
    # tests in valid input is parsed correctly
    def test_parse_input(self):
        input_str = "1, 2-5"
        res = parse_input(input_str)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0].start, 1)
        self.assertEqual(res[0].end, 1)
        self.assertEqual(res[1].start, 2)
        self.assertEqual(res[1].end, 5)

    # tests if empty input throws ValueError
    def test_empty_input(self):
        input_str = ""
        try:
            parse_input(input_str)
        except ValueError as e:
            pass
        except Exception as e:
            self.fail("Expected ValueError to be raised")
        else:
            self.fail("Expected ValueError to be raised")

    # tests if invalid input throws ValueError
    def test_parse_input_throws_ValueError_if_invalid(self):
        input_str = "1, s"
        try:
            parse_input(input_str)
        except ValueError as e:
            pass
        except Exception as e:
            self.fail("Expected ValueError to be raised")
        else:
            self.fail("Expected ValueError to be raised")

    # tests for empty input
    def test_empty_intervals(self):
        input = []
        res = merge_intervals(input)
        self.assertEqual(len(res), 0)

    # tests for non overlapping intervals
    def test_merge_interval_if_disjoint(self):
        input = [Interval("1"), Interval("2", "5"), Interval("6", "10")]
        res = merge_intervals(input)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0].start, 1)
        self.assertEqual(res[0].end, 1)

        self.assertEqual(res[1].start, 2)
        self.assertEqual(res[1].end, 5)

        self.assertEqual(res[2].start, 6)
        self.assertEqual(res[2].end, 10)

    # tests if overlapping intervals are merged
    def test_merge_interval_if_overlapping(self):
        input = [Interval("1"), Interval("2", "6"), Interval("5", "10"), Interval("12", "15")]
        res = merge_intervals(input)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0].start, 1)
        self.assertEqual(res[0].end, 1)

        self.assertEqual(res[1].start, 2)
        self.assertEqual(res[1].end, 10)

        self.assertEqual(res[2].start, 12)
        self.assertEqual(res[2].end, 15)

    # tests if merged correctly when preceding interval has higher range
    def test_merge_interval_if_overlapping_and_preceding_range_greater(self):
        input = [Interval("1"), Interval("2", "10"), Interval("5", "9")]
        res = merge_intervals(input)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0].start, 1)
        self.assertEqual(res[0].end, 1)

        self.assertEqual(res[1].start, 2)
        self.assertEqual(res[1].end, 10)

    # tests if nerged correctly when unsorted intervals present
    def test_merge_interval_if_overlapping_unsorted(self):
        input = [Interval("1"), Interval("5", "12"), Interval("3", "9")]
        res = merge_intervals(input)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0].start, 1)
        self.assertEqual(res[0].end, 1)

        self.assertEqual(res[1].start, 3)
        self.assertEqual(res[1].end, 12)

