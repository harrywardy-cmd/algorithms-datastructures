class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            L = 1                              #L pointer is pointing to all unique values, start at 1 bc 0 will not need to be swapped
            for R in range(1, len(nums)):
                if nums[R] != nums[R - 1]:      #will check the the R pointer and the previous value is they are diffrent 
                    nums[L] = nums[R]            # if they are, replace the value on the L pointer with the R pointer then itterate L and exit the if statment
                    L += 1

            return L                            #L will show the total of values and K
