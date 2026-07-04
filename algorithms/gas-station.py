class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If the total amount of gas is less than the total cost,
        # it is impossible to complete the circuit.
        if sum(gas) < sum(cost):
            return -1

        # Tracks the current amount of gas left in the tank.
        gas_amount = 0

        # Stores the current candidate starting gas station.
        result = 0

        # Traverse each gas station once.
        for i in range(len(cost)):
            # Fill up at the current station, then spend gas
            # to travel to the next station.
            gas_amount = (gas_amount + gas[i]) - cost[i]

            # If we run out of gas, then none of the stations
            # from 'result' to 'i' can be a valid starting point.
            if gas_amount < 0:
                # Try the next station as the new starting point.
                result = i + 1

                # Reset the gas tank for the new attempt.
                gas_amount = 0

        # Return the valid starting station.
        return result
