class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Stack to keep track of all valid scores
        score = []

        # Process each operation in order
        for op in operations:
            if op == '+':
                # Add a new score equal to the sum of the previous two scores
                score.append(score[-1] + score[-2])

            elif op == 'D':
                # Add a new score that is double the previous score
                score.append(score[-1] * 2)

            elif op == 'C':
                # Remove the most recent valid score
                score.pop()

            else:
                # Convert the string to an integer and record it as a new score
                score.append(int(op))

        # Return the total score after processing all operations
        return sum(score)
