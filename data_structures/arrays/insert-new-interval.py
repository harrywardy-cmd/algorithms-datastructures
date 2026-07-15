class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int]
    ) -> List[List[int]]:

        # Stores the final list of merged intervals.
        result = []

        # Loop through each existing interval.
        for i in range(len(intervals)):

            # Case 1:
            # The new interval comes completely before the current interval.
            #
            # Since the intervals are sorted, there can be no more overlaps.
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)

                # Add all remaining intervals and return immediately.
                return result + intervals[i:]

            # Case 2:
            # The new interval comes completely after the current interval.
            elif newInterval[0] > intervals[i][1]:

                # The current interval does not overlap,
                # so add it directly to the result.
                result.append(intervals[i])

            # Case 3:
            # The new interval overlaps with the current interval.
            else:

                # Merge the two intervals by taking:
                # - The smallest starting point.
                # - The largest ending point.
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # If the new interval was not inserted during the loop,
        # add the final merged interval to the result.
        result.append(newInterval)

        # Return the sorted and merged intervals.
        return result
