class Solution:
    def scoreOfString(self, s: str) -> int:

        ascii_values = [ord(char) for char in s]

        i = 0
        j = 1
        result = 0

        while j > i:

            if j > len(ascii_values) - 1:
                break

            if ascii_values[j] >= ascii_values[i]:
                result += (ascii_values[j] - ascii_values[i])
            else:
                result += (ascii_values[i] - ascii_values[j])

            i += 1
            j += 1


        return result

