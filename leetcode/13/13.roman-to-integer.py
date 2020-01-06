#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
# Author: Liu Song

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. 找到相应的pattern
        # 2. 将pattern给算出结果后除掉.
        # 3. 将剩下的普通字符解释成数字即可

        res = 0
        pattern_idx = s.find('IV')
        while(pattern_idx != -1):
            if not s: return res
            res += 4
            s = s[:pattern_idx] + s[pattern_idx+2:]
            pattern_idx = s.find('IV')
        

        pattern_idx = s.find('IX')
        while(pattern_idx != -1):
            if not s: return res
            res += 9
            s = s[:pattern_idx] + s[pattern_idx+2:]
            pattern_idx = s.find('IX')
        
        pattern_idx = s.find('XL')
        while(pattern_idx != -1):
            if not s: return res
            res += 40
            s = s[:pattern_idx] + s[pattern_idx+2:]
            pattern_idx = s.find('XL')

        pattern_idx = s.find('XC')
        while(pattern_idx != -1):
            if not s: return res
            res += 90
            s = s[:pattern_idx] + s[pattern_idx+2:]
            pattern_idx = s.find('XC')

        pattern_idx = s.find('CD')
        while(pattern_idx != -1):
            if not s: return res
            res += 400
            s = s[:pattern_idx] + s[pattern_idx+2:]
            pattern_idx = s.find('CD')

        pattern_idx = s.find('CM')
        while(pattern_idx != -1):
            if not s: return res
            res += 900
            s = s[:pattern_idx] + s[pattern_idx+2:]
            pattern_idx = s.find('CM')

        for c in s:
            if c == 'I': res += 1
            elif c == 'V': res += 5
            elif c == 'X': res += 10
            elif c == 'L': res += 50
            elif c == 'C': res += 100
            elif c == 'D': res += 500
            elif c == 'M': res += 1000

        return res    
    def test(self):
        # print(self.romanToInt('III'))
        assert(self.romanToInt('III') == 3)
        assert(self.romanToInt('IV') == 4)
        assert(self.romanToInt('IX') == 9)
        assert(self.romanToInt('LVIII') == 58)
        assert(self.romanToInt('MCMXCIV') == 1994)

so = Solution()
so.test()
# @lc code=end

