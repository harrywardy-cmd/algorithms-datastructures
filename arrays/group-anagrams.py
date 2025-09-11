class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)        #uses a defultdict to avoid errors where the value is not in the dict 

        for s in strs:
            count =[0] * 26            # using this as a key which shows the frequency of characters in array 
                                       # with the posion of the array being the letter and the value being the frequency( h = 8th value, as h is the 8th letter in the alphabet)  
            for c in s:
                count[ord(c) - ord("a")] += 1      # uses the ASCII values to find the position of the letter in the array and iterates the frequency
            res[tuple(count)].append(s)            #finds the count array in the dict and adds the anagram (has to be a tuple as they are immutable)

        return list(res.values())                  # this will return just the values from our dict 
