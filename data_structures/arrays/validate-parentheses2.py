class Solution:
    def isValid(self, s: str) -> bool:
        # Stack used to keep track of opening brackets.
        stack = []

        # Dictionary that maps each closing bracket
        # to its corresponding opening bracket.
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Iterate through every character in the string.
        for c in s:
            # If the current character is a closing bracket...
            if c in closeToOpen:
                # Check if the stack is not empty and the top of the stack
                # contains the matching opening bracket.
                if stack and stack[-1] == closeToOpen[c]:
                    # Matching pair found, remove the opening bracket.
                    stack.pop()
                else:
                    # Either the stack is empty or the brackets don't match.
                    return False
            else:
                # Current character is an opening bracket,
                # so push it onto the stack.
                stack.append(c)

        # If the stack is empty, every opening bracket
        # had a matching closing bracket.
        return not bool(stack)
