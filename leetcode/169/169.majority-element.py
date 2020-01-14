#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: []) -> int:
        threshold = len(nums) // 2
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
                continue
            nums_dict[num] += 1

        for num, times in nums_dict.items():
            if times > threshold:
                return num

    def test(self):
        assert(self.majorityElement([3,2,3]))
        assert(self.majorityElement([2,2,1,1,1,2,2]))

sol = Solution()
sol.test()
# @lc code=end

