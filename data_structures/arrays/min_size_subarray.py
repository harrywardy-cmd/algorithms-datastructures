class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        L = 0
        length = len(nums) + 1

        for R in range(len(nums)):
            total += nums[R]  

            while total >=target:                  #check if we have gone over or reached our total
                length = min (R-L +1, length)      # check if our current length is smaller then our stored length
                total -= nums[L]                   # remove the first value added breaking the while loop
                L += 1                            
        
        return 0 if length == len(nums) + 1 else length
