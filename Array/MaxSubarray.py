# https://leetcode.com/problems/maximum-subarray/description/?envType=problem-list-v2&envId=vxb9dsfm
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        soma_total = soma_atual = nums[0]
        inicio = fim = temp_inicio = 0

        for i in range(1, len(nums)):
           ## Verifica se o número por si só é maior que a soma atual com ele mesmo
           ## A partir disso, inicia-se um novo subvetor
           if nums[i] > soma_atual + nums[i]:
                soma_atual = nums[i]
                temp_inicio = i # começa novo subvetor
           else:
                soma_atual += nums[i]
           ## Vai salvando soma_atual temporariamente
           if soma_atual > soma_total:
                soma_total = soma_atual
                inicio = temp_inicio
                fim = i
            
        subvetor_max = nums[inicio:fim+1]
        return soma_total