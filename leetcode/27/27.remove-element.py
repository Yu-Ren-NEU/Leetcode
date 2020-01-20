#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
# Author: Liu Song

# @lc code=start
class Solution:
    def removeElement(self, nums: [], val: int) -> int:
        # 貌似跟26号题是一样的.
        # 26号是去除重复
        # 27号题是去除给定的元素
        
        while(val in nums):
            nums.remove(val)
        
        # print(nums)
        return len(nums)

    def test(self):
        testcase = [0,1,2,2,3,0,4,2]
        print(self.removeElement(testcase, 2))

# sol = Solution()
# sol.test()
        
# @lc code=end

