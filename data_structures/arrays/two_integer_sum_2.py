class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R = 0,len(numbers) - 1                 #sets two pointers

        while L<R:                                #while each pointer is not at the same position
            if numbers[R] + numbers[L] < target:  #if the sum of L and R are smaller then the target, move the left pointer to the rigth to increase the sum of L and R
                L += 1
            elif numbers[R] + numbers[L] > target:  # else the sum is larger then the target, then move the R pointer to the left to decrease the sum of L and R
                R -= 1
            else:
                return [L+1,R+1]                    #return the position of L and R
