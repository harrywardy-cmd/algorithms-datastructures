class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # Check every character in every row
        for row in range(len(words)):
            for col in range(len(words[row])):

                # For a valid word square:
                # words[row][col] must equal words[col][row]
                #
                # Before comparing, make sure:
                # 1. The corresponding row exists.
                # 2. The corresponding column position exists in that row.
                if (
                    col >= len(words)
                    or row >= len(words[col])
                    or words[row][col] != words[col][row]
                ):
                    return False

        # All characters matched their transposed positions
        return True
