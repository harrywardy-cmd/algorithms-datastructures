class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = set()
        length = 0
        L = 0                        #using two point(sliding window), L is here and R is set through the for loop

        for R in range(len(s)):
            while s[R] in string:            #if s[R] is in the hash set it will remove it from the hash set and increment the left pointer on the s (the string)
                string.remove(s[L])
                L += 1
            string.add(s[R])                #when there no more characters left with the value of the right pointer from the left pointer position, it will add the value of the right pointer to the hash set
            length = max(R - L + 1, length) # this will compare the length of the old substring with the current one and set the value of length

        return length                        #will return the biggest substring 
            
