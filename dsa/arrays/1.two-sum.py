#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#s

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sol = {}
        for ind, val in enumerate(nums):
            missing = target - val
            if missing in sol.keys():
                return [sol[missing], ind]
            sol[val] = ind
 
# @lc code=end

