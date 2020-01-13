#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: []) -> int:
        # 找出单个而非成对的数字
        # 那我只需要存一张表就可以了. 
        single = []
        for num in nums:
            if num not in single:
                single.append(num)
            else:
                single.remove(num)
        return single[0]

    def test(self):
        print(self.singleNumber([4,1,2,1,2]))

sol = Solution()
sol.test()
# @lc code=end

