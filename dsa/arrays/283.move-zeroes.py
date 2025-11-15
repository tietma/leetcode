#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l_p = 0

        for ind in range(0, len(nums)):
            if nums[ind] != 0:
                nums[l_p], nums[ind] = nums[ind], nums[l_p]
                l_p += 1

