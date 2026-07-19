class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets.
        stack = []

        # Maps each closing bracket to its matching opening bracket.
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Iterate through every character in the string.
        for c in s:
            # If the character is a closing bracket...
            if c in closeToOpen:
                # Check that:
                # 1. The stack is not empty.
                # 2. The top of the stack contains the matching opening bracket.
                if stack and stack[-1] == closeToOpen[c]:
                    # Matching pair found, remove the opening bracket.
                    stack.pop()
                else:
                    # No matching opening bracket, so the string is invalid.
                    return False
            else:
                # Opening bracket found, push it onto the stack.
                stack.append(c)

        # The string is valid only if all opening brackets
        # have been matched and the stack is empty.
        return not bool(stack)
