#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
# Author: Liu Song

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数肯定不是回文
        # 0肯定是回文

        if x < 0: return False
        if x == 0: return True

        # 1. 将正数转换成字符串
        # 2. 因为python支持负索引,所以可以直接用来检查回文
        # 3. 但是要注意索引不要越界
        input_str = str(x)
        length = len(input_str)
        for idx in range(length//2+1):
            if input_str[idx] != input_str[-idx-1]:
                return False
        return True

    def test(self):
        assert(self.isPalindrome(121) == True)
        assert(self.isPalindrome(-121) == False)
        assert(self.isPalindrome(10) == False)

sol = Solution()
sol.test()
# @lc code=end

