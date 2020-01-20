#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 思路就是去除掉非ascii字符
        import string
        
        target = ''
        for c in s.lower():
            if c in string.ascii_lowercase+string.digits:
                target += c

        # 空字符串
        if not target: return True
        length = len(target)

        for idx in range(length//2+1):
            # print(target[idx], target[-idx-1])
            if target[idx] != target[-idx-1]:
                return False
        return True

    def test(self):
        assert(self.isPalindrome("") == True)
        assert(self.isPalindrome(" ") == True)
        assert(self.isPalindrome("0P") == False)
        assert(self.isPalindrome("0P0") == True)
        assert(self.isPalindrome("0P1") == False)
        assert(self.isPalindrome("A man, a plan, a canal: Panama") == True)
        assert(self.isPalindrome("race a car") == False)

sol = Solution()
sol.test()
# @lc code=end

