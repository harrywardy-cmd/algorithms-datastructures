from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Store all students in a queue so they can move from the
        # front to the back if they don't want the current sandwich.
        q = deque(students)

        # Total number of students currently without a sandwich.
        res = len(students)

        # Process each sandwich from the top of the sandwich stack.
        for sandwich in sandwiches:
            # Count how many students have been rotated.
            # If every remaining student has been checked and none
            # want the current sandwich, no further sandwiches can
            # be eaten.
            count = 0

            # Keep rotating students until someone wants the sandwich
            # or every remaining student has been checked.
            while count < len(q) and q[0] != sandwich:
                student = q.popleft()   # Remove student from the front.
                q.append(student)       # Move them to the back.
                count += 1

            # If the student at the front likes the sandwich,
            # they take it and leave the queue.
            if q and q[0] == sandwich:
                q.popleft()
                res -= 1
            else:
                # No student wants the current sandwich.
                # Since the sandwich order cannot change,
                # no more students can eat.
                break

        # Return the number of students who could not eat.
        return res
