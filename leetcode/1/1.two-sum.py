#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ! 可能有相同的元素.

        nums_dict = {} 
        for idx, num in enumerate(nums):
            if num in nums_dict:
                return [nums_dict[num], idx]
            else:
                nums_dict[target - num] = idx
# @lc code=end