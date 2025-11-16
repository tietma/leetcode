#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l_ind = 0

        for ind in range(0, len(nums)):
            if nums[ind] != val:
               nums[ind], nums[l_ind] = nums[l_ind], nums[ind]
               l_ind += 1

        return l_ind 
# @lc code=end

