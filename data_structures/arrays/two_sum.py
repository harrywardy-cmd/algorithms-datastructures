#- Two Sum
#- Problem: [LeetCode #1](https://leetcode.com/problems/two-sum/)
#- Approach: Hashmap one pass through
#- Time: O(n), Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}                                            # val -> index, create a hash map

        for i, n in enumerate(nums):
            diff = target - n                                   # find the difference of 'target - current number'
            if diff in prevMap:                                 # if the difference is in the hash map return the position of diff in the hashmap and i (the current position)
                return [prevMap[diff], i]                       
            prevMap[n] = i                                      #else add the number into our hashmap


#Input: 
#nums = [3,4,5,6], target = 7

#Output: [0,1]