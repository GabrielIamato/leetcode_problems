# https://leetcode.com/problems/rotate-array/
class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        n = len(nums)
        k = k % len(nums)
        # Reverter array todo
        reverse(0, n-1)
        # Reverter k primeiros
        reverse(0, k-1)
        # Reverter k ultimos
        reverse(k, n-1)
        return nums


        