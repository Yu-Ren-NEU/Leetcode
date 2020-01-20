#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
# Author: Liu Song

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # ! 首先空字符串是合法的
        if s == '': return True

        # 匹配括号
        # ! 首先需要考虑括号的顺序
        # 用栈来保存左括号, 也就是([{ 
        # 当遇到右括号, 也就是}]), 立马弹栈匹配
        # 如果弹出的括号不能匹配, 那么就是不合法的
        
        # ! 考虑栈不能为空的时候pop
        stack = []
        for chr in s:
            if chr in ['[', '(', '{']:
                # 遇到了左括号
                stack.append(chr)
            else:
                # 遇到了右括号
                if not stack:
                    # 此时栈已经空了
                    return False
                # 以下是栈未空的情况, 弹栈出来匹配
                left = stack.pop()
                if chr == ']' and left != '[': return False
                elif chr == ')' and left != '(': return False
                elif chr == '}' and left != '{': return False

        # 仍然要考虑栈为空的情况
        # 必须当栈已经空了, 才是正确的. 
        # 否则比如 '[' 会误判为正确的
        if not stack: return True
        else: return False

    def test(self):
        testcase = "()"
        testcase2 = "()[]{}"
        testcase3 = "(]"
        testcase4 = "([)]"
        testcase5 = "{[]}"
        testcase6 = ''
        testcase7 = '['

        assert(self.isValid(testcase) == True)
        assert(self.isValid(testcase2) == True)
        assert(self.isValid(testcase3) == False)
        assert(self.isValid(testcase4) == False)
        assert(self.isValid(testcase5) == True)
        assert(self.isValid(testcase6) == True)
        assert(self.isValid(testcase7) == False)

sol = Solution()
sol.test()

# @lc code=end

