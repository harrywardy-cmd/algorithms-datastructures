class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        # Start from the second element and compare it with the previous element
        for i in range(1, len(nums)):
            
            # Check if both adjacent numbers have the same parity
            # % 2 returns 0 for even numbers and 1 for odd numbers
            if nums[i - 1] % 2 == nums[i] % 2:
                
                # If both numbers are even or both are odd,
                # the array is not special
                return False
        
        # Every adjacent pair has different parity,
        # so the array is special
        return True
