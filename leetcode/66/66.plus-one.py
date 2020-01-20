#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: []) -> []:
        # 思路很简单
        # 把list转换成字符串, 然后字符串转数字
        # 然后数字加1 再映射成字符串, 组合成list
        return list(map(int, str(int("".join([str(elem) for elem in digits])) + 1))) 
        
    def test(self):
        assert(self.plusOne([1,2,3]) == [1,2,4])
        assert(self.plusOne([4,3,2,1]) == [4,3,2,2])

sol = Solution()
sol.test()

# @lc code=end

