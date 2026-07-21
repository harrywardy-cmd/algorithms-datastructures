"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort all meetings by their start time
        # This allows us to compare each meeting with the one before it
        intervals.sort(key=lambda i: i.start)

        # Iterate through the sorted meetings starting from the second meeting
        for i in range(1, len(intervals)):
            # Previous meeting
            i1 = intervals[i - 1]

            # Current meeting
            i2 = intervals[i]

            # If the previous meeting ends after the current meeting starts,
            # the meetings overlap and it is impossible to attend both
            if i1.end > i2.start:
                return False

        # No overlapping meetings were found
        return True
