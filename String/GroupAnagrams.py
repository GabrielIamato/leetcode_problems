# https://leetcode.com/problems/group-anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grupos = defaultdict(list)
        for palavra in strs:
            chave = ''.join(sorted(palavra))
            grupos[chave].append(palavra)
        return list(grupos.values())
        