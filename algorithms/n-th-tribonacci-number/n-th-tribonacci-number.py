class Solution:
    def tribonacci(self, n: int) -> int:
        # Store the first three Tribonacci numbers:
        # T0 = 0, T1 = 1, T2 = 1
        trip = [0, 1, 1]

        # If n is one of the first three numbers,
        # return it directly from the array.
        if n < 3:
            return trip[n]

        # Start calculating from T3 up to Tn.
        for i in range(3, n + 1):

            # Shift the previous values to the left:
            # T0 becomes T1
            # T1 becomes T2
            # T2 becomes T0 + T1 + T2
            #
            # The right-hand side is evaluated first,
            # so we don't lose the previous values.
            trip[0], trip[1], trip[2] = (
                trip[1],
                trip[2],
                sum(trip)
            )

        # The third position contains the final Tribonacci number.
        return trip[2]
