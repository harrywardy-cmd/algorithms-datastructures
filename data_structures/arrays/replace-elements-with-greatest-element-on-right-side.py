class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        highest = -1
        temp =0

        i = len(arr) -1

        while i >= 0 :
            if arr[i] > highest:
                temp = arr[i]
                arr[i] = highest
                highest = temp

            else:
                arr[i] = highest
            i -= 1
            

        return arr


            
            
