# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {} # obtem ultimo indice de cada caractere
        inicio = 0
        maior_substring = 0

        for i, char in enumerate(s):
            if char in char_index and char_index[char]>=inicio:
                inicio = char_index[char]+1
            char_index[char] = i
            maior_substring = max(maior_substring, i - inicio + 1)
        return maior_substring

        