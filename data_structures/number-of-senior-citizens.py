class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # Keep track of how many passengers are older than 60
        result = 0

        # Check each passenger's encoded details
        for i in details:
            # Extract the age (characters at index 11 and 12)
            # Convert it to an integer and count if age is greater than 60
            if int(i[11:13]) > 60:
                result += 1

        # Return the total number of senior passengers
        return result
