# 
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
# Author: Liu Song

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # 输入有32位
        # ! 输入可能是负数, 负号无需反向
        # ! 输入可能带有0, 反向时需要考虑
        # ! 注意, 当翻转后的数字溢出32位时要返回0

        # 1. 判断输入的正负, 用于处理负号 
        # 2. 将数字转换成字符串
        # 3. 对字符串进行反向
        # 4. 将反向后的字符串转换成整数
        if x < 0:
            tmp = str(-x)
            tmp = tmp[::-1]
            tmp = int(tmp)
            tmp = -tmp
        else:
            tmp = str(x)
            tmp = tmp[::-1]
            tmp = int(tmp)
        
        if tmp < -pow(2, 31) or tmp > (pow(2, 31)-1):
            return 0

        return tmp

    def test(self):
        assert(self.reverse(123) == 321)
        assert(self.reverse(-123) == -321)
        assert(self.reverse(120) == 21)
        assert(self.reverse(1534236469) == 0)
# @lc code=end

