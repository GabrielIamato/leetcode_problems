# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapa = {}
        for i, valor in enumerate(nums):
            # Calcula o complemento do target
            complemento = target - valor
            # Se o complemento já foi passado, retorna o índice dele
            if complemento in mapa:
                # mapa[complemento] retorna o índice de "complemento"
                return[mapa[complemento], i] 
            # Se não achou nos valores já percorridos, insere em mapa
            mapa[valor] = i

