class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Store every coordinate we've visited.
        # We use a hash of (x, y) instead of storing tuples.
        seen = set()

        # Start at the origin (0, 0).
        x, y = 0, 0

        # Mark the starting position as visited.
        seen.add(self.hash(x, y))

        # Process each movement in the path.
        for c in path:

            # Move one unit in the specified direction.
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            elif c == 'W':
                x -= 1

            # Generate a unique hash for the new position.
            pos = self.hash(x, y)

            # If we've already visited this position,
            # the path crosses itself.
            if pos in seen:
                return True

            # Otherwise, record this position.
            seen.add(pos)

        # No position was visited more than once.
        return False

    def hash(self, x: int, y: int) -> int:
        # Combine the x and y coordinates into a single integer.
        # Shift x left by 32 bits so it occupies the upper half,
        # then add y in the lower half.
        # This creates a unique value for each (x, y) coordinate pair.
        return (x << 32) + y
