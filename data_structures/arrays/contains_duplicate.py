class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkednums = set()

        for x in nums:              
            if x in checkednums:       #will check if number was in the hashset and return true
                return True
            checkednums.add(x)         #add numbers to hashset
            
        return False                    #if the for loop doesnt return true, it will return false as the loop did not find any duplicates
