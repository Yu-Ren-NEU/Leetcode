#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
# Author: Liu Song

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: []) -> str:
        # 1. 先求idx的最大值, 也就是最短的字符串长度
        # 2. idx从0开始增长进行切片        
        # 3. 将各个字符串的切片合成set判断长度即可. 
        prefix = ''
        idx = 0
        max_idx = 100000000
        for item in strs:
            if len(item) < max_idx:
                max_idx = len(item)
        # print(max_idx)

        is_whole_word = False
        while(len(set([x[:idx] for x in strs])) == 1):
            if idx > max_idx-1: 
                is_whole_word = True
                break
            prefix += strs[0][idx]
            idx += 1
        if is_whole_word: return prefix

        # 多加了一个字符
        return prefix[:len(prefix)-1]

    def test(self):
        testcase =  ["flower","flow","flight"]
        testcase2 = ["dog","racecar","car"]
        testcase3 = ["flower", "flower", "flower2"]
        assert(self.longestCommonPrefix(testcase) == "fl")
        assert(self.longestCommonPrefix(testcase2) == "")

        assert(self.longestCommonPrefix(testcase3) == "flower")
        


sol = Solution()
sol.test()
# @lc code=end

