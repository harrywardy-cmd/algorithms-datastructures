class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        highest = -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = highest
            highest = max(highest, current)

        return arr
