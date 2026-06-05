class Solution:

    def encode(self, strs: List[str]) -> str:  #encode with the length of the word followed by "#", connectingt he rest of the stings into on string
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]: # it will read the stings, find "#" then find the number(length of the word) and decode the length and add to an array 
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
