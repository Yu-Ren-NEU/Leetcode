#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
# Author: Liu Song

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: []) -> int:
        # 我人晕了. 不能用set直接把list去重
        # 必须得改变nums
        # 因为给定的list是已经排好序的
        # 所以只要比较相邻元素, 如果相邻元素相等, 把元素除去即可.

        # ! 注意索引不要越界
        idx = 0
        max_idx = len(nums)-1
        while True:
            if idx+1 > len(nums)-1: break

            if nums[idx] == nums[idx+1]:
                nums.pop(idx+1)
                # 且慢, 重复的值可能不止1个
                # 所以这里要将索引恢复成上一个
                idx -= 1
            idx += 1

        return len(nums)

    def test(self):
        testcase = [0,0,1,1,1,2,2,3,3,4]
        print(self.removeDuplicates(testcase))

sol = Solution()
sol.test()
# @lc code=end

