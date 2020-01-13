#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> [[]]:
        # 当numRows为0时, 返回空list
        if not numRows: return []
        elif numRows == 1: return [[1]]
        elif numRows == 2: return [[1], [1,1]]

        # 注意为result开辟空间
        result = [[1], [1,1]]
        
        depth = 2
        while( depth < numRows ):            
            prev_row = result[depth-1]
            prev_row_len = len(prev_row)
            prev_idx = 1
            
            next_row = [1]
            while(prev_idx < prev_row_len):
                next_elem = prev_row[prev_idx-1] + prev_row[prev_idx]
                next_row.append(next_elem)
                prev_idx += 1
            next_row.append(1)

            depth += 1
            result.append(next_row)
        return result

    def test(self):
        print(1, self.generate(1))
        print(2, self.generate(2))
        print(3, self.generate(3))
        print(4, self.generate(4))
        print(5, self.generate(5))


# sol = Solution()
# sol.test()
# @lc code=end

