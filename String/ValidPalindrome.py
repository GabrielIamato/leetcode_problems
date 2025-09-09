# https://leetcode.com/problems/valid-palindrome/
import unicodedata
class Solution(object):
    def limpar_string(self, s):
        return ''.join(
            c.lower()
            for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn' and c.isalnum()
        )
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.limpar_string(s)
        for i in range(0, len(s)/2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

        