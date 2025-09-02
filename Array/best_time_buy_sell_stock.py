#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        complemento_maior = 0
        maior = prices[len(prices) - 1]

        for i, valor in enumerate(reversed(prices)):
            complemento_aux = maior - valor

            if complemento_aux > complemento_maior:
                complemento_maior = complemento_aux

            if valor > maior:
                maior = valor

        return complemento_maior