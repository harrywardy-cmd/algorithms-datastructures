class Solution:
    def findLucky(self, arr: List[int]) -> int:

        # Dictionary to store the frequency of each number
        my_dict = {}

        # Default result is -1 if no lucky number is found
        result = -1

        # Count how many times each number appears
        for i in arr:
            my_dict[i] = my_dict.get(i, 0) + 1

        # Check each number and its frequency
        for i in my_dict:

            # A lucky number appears exactly as many times as its value
            if i == my_dict[i]:

                # Keep the largest lucky number found
                result = max(my_dict[i], result)

        # Return the largest lucky number, or -1 if none exists
        return result
