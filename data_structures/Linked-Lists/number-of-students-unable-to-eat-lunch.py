class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)

        res = n
        for sandwitch in sandwiches:    #will itterate through the types of sandwitches
            count = 0
            while count < n and q[0] != sandwitch:  #if the studend doesnt like the sandwitch the will move to the back of the queue
                cur = q.popleft()
                q.append(cur)
                count += 1
            if q[0] == sandwitch:                 #if they like the sandwitch they will be popped from the queue and n (the total amount of students with out a sandwitch) will decrease
                q.popleft()
                res -= 1
            else:
                break
        return res                    #return the total amount of students without a sandwitch
