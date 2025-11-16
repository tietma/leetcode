#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_i = 0

        for ind in range(1,len(nums)):
            if nums[ind] != nums[l_i]:
                l_i += 1
                nums[l_i] = nums[ind]

        return l_i+1

# @lc code=end

