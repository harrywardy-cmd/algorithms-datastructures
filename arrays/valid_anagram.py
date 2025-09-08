class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # both strings will have to be the same length 
            return False

        countS, countT = {}, {} # creates hashmap

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # add the letters to the hashmap as the key and the frequency as the value
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT #this will compare each hashmap
