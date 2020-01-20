#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:

    def countAndSay(self, n: int) -> str:
        if n == 1:  return '1'
        return self.get(self.countAndSay(n-1))

    def get(self, n: int) -> str:
        # * 看了一段时间才看懂题目
        # * 也就是n+1项是在描述第n项
        # * 那么显然是存在递归推导关系
        # * 想办法把最开头的关系弄清楚, 就能推导后面n项的值
        # ! 1. 首先考虑有多少种解释的情形
        # *   1   -> 11   -> 初始情况 a   -> 1a
        # *   2   -> 12   -> 初始情况 a   -> 1a
        # *   11  -> 21   -> 连续情况 n个a    -> na
        # *   12  -> 11 12    -> 不连续   -> 单独解释
        # *   21  -> 12 11    -> 不连续   -> 单独解释
        # *   22  -> 22   -> 连续情况 n个a    -> na 

        # ! 2. 关系就是
        # *   不连续出现的单个数字 a -> 1a
        # *   连续出现的多个数字  aaa -> 3a, 3是a出现的次数
        
        # ! 3. 开始解析, 要分两个索引
        # *   一个索引当前数字, 一个索引之后的数字

        seq = str(n)
        seq_len = len(seq)
        if seq_len == 1:
            return '1'+seq

        
        curr_idx = 0
        count = 1
        next_idx = curr_idx + count
        if (seq[next_idx] != seq[curr_idx]):
            left = self.get(seq[curr_idx])
            right = self.get(seq[next_idx:])
            # print(seq[curr_idx], seq[next_idx:])
            return left + right
        else:
            # print('pass')
            while (seq[next_idx] == seq[curr_idx]):
                next_idx += 1
                if next_idx > seq_len-1: break
                count += 1

            if next_idx < seq_len:
                left = str(count) + seq[curr_idx]
                right = self.get(seq[next_idx:])
                return left + right
            else:
                # ! 边界检查
                # 此时next_idx > seq_len-1
                # 还需再加1

                count += 1
                return str(count) + seq[curr_idx]

    def test(self):
        assert(self.get(1) == '11')
        assert(self.get(2) == '12')
        assert(self.get(11) == '21')
        assert(self.get(12) == '1112')
        assert(self.get(22) == '22')
        assert(self.get(21) == '1211')
        assert(self.get(1211) == '111221')
        assert(self.get(111221) == '312211')
        assert(self.get(312211) == '13112221')
    
    def test2(self):
        assert(self.countAndSay(1) == '1')
        assert(self.countAndSay(2) == '11')
        assert(self.countAndSay(3) == '21')
        assert(self.countAndSay(4) == '1211')
        assert(self.countAndSay(5) == '111221')

sol = Solution()
sol.test2()



# @lc code=end

