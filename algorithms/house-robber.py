class Solution:
    def rob(self, nums: List[int]) -> int:
        # house1 = Maximum money that can be robbed up to two houses ago
        # house2 = Maximum money that can be robbed up to the previous house
        house1, house2 = 0, 0

        # Iterate through each house
        for money in nums:
            # Decide whether to:
            # 1. Rob the current house (money + house1)
            # 2. Skip the current house (house2)
            max_rob = max(money + house1, house2)

            # Shift the window forward:
            # house1 becomes the previous maximum (house2)
            house1 = house2

            # house2 stores the best result up to the current house
            house2 = max_rob

        # Return the maximum amount that can be robbed
        return house2
