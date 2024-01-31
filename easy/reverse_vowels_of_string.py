class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        split_string = list(s)
        string_vowels = []

        for char in split_string:
                if char in vowels:
                    string_vowels.append(char)

        if len(s) > 1 and len(string_vowels) > 1:
            reversed_string_vowels = []
            reversed_string_vowels = string_vowels[::-1]

            i = 0
            for char in split_string:
                if len(string_vowels) > 0 and split_string[i] == string_vowels[0]:
                    split_string[i] = reversed_string_vowels[0]
                    string_vowels.pop(0)
                    reversed_string_vowels.pop(0)
                i += 1
            return ''.join(split_string)
        else:
            return s