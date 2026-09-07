class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        # Create a dictionary to keep track of how many times
        # each character needed to spell "balloon" appears.
        my_dict = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }

        # Go through every character in the input string.
        for key in text:

            # Only count characters that are needed to spell "balloon".
            if key in my_dict:

                # Increase the count for the current character by 1.
                my_dict[key] = my_dict.get(key, 0) + 1

        # "balloon" requires:
        # - 1 'b'
        # - 1 'a'
        # - 2 'l'
        # - 2 'o'
        # - 1 'n'
        #
        # Divide the 'l' and 'o' counts by 2 because
        # each "balloon" needs two of each.
        #
        # The smallest available count determines how many
        # complete "balloon" words we can create.
        return min(
            my_dict['b'],
            my_dict['a'],
            my_dict['l'] // 2,
            my_dict['o'] // 2,
            my_dict['n']
        )
