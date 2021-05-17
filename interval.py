from typing import List


class Interval:
    def __init__(self, start: str, end: str = None):
        self.start = int(start.strip())
        if end is None:
            self.end = self.start
        else:
            self.end = int(end.strip())

    def __str__(self):
        if self.start == self.end:
            return str(self.start)
        return str(self.start) + "-" + str(self.end)


def parse_input(input_str):
    """
    Given a string, parses it and returns a list of intervals
    Args:
        input_str (str): String to parse
    Returns:
         List[Interval]: List of parsed interval objects
    Raises:
        ValueError: If the string does not represent a set of valid intervals
    """
    res: List[Interval] = []

    intervals_arr: List[str] = input_str.split(",")

    for each in intervals_arr:
        if "-" not in each:
            interval = Interval(each)
            res.append(interval)
        else:
            interval_arr: List = each.split("-")
            res.append(Interval(interval_arr[0], interval_arr[1]))

    return res


def merge_intervals(intervals: List[Interval]):
    """
    Given a list of intervals, returns a new list with overlapping/adjacent intervals merged
    :param intervals:
    :return: List[Interval]: List of intervals where no intervals overlap
    """
    intervals.sort(key=lambda x: x.start)

    res = []
    for each in intervals:
        if not res or res[-1].end < each.start:
            res.append(each)
        else:
            res[-1].end = max(res[-1].end, each.end)

    return res


def print_intervals(intervals: List[Interval]):
    return ", ".join(map(lambda x: str(x), intervals))
