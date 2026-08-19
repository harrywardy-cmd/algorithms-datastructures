class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Store words that are found as substrings of another word
        res = []

        # Sort words by length so shorter words are checked first
        words.sort(key=len)

        # Loop through each word
        for i in range(len(words)):

            # Compare the current word with every longer word
            for j in range(i + 1, len(words)):

                # Check if the current word is a substring of words[j]
                if words[i] in words[j]:
                    # Add the word to the result
                    res.append(words[i])

                    # Stop checking this word once a match is found
                    break

        # Return all words that were found inside another word
        return res
