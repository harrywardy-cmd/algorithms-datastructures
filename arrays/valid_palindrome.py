class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1    # puts pointer on the start and end of the string

        while l < r:
            while l < r and not self.alphaNum(s[l]):    #while l is less then r and is not alphanumeric, it will itterate through
                l += 1
            while r > l and not self.alphaNum(s[r]):    #while r is less then l and is not alphanumeric, it will itterate through
                r -= 1
            if s[l].lower() != s[r].lower():            # will check that the lower case of the letters are the same if not return false 
                return False
            l, r = l + 1, r - 1                         #will move both pointers
        return True

    def alphaNum(self, c):             #used to check if the letter is alphanumeric 
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
