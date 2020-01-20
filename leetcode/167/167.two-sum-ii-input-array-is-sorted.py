#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: [], target: int) -> []:
        num_dict = {}
        for idx, num in enumerate(numbers):
            if num in num_dict:
                return [num_dict[num]+1, idx+1]
            else:
                num_dict[target-num] = idx
    def test(self):
        assert(self.twoSum([2,7,11,15], 9) == [1,2])

sol = Solution()
sol.test()

# @lc code=end

