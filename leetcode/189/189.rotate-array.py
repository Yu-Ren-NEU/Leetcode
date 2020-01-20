#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: [], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return []

        # 实质上是将队尾元素移除, 然后重新插入到队首
        for idx in range(k):
            last_elem = nums.pop()
            nums.insert(0, last_elem)
            idx += 1 
        # print(nums)
    def test(self):
        self.rotate([1,2,3,4,5,6,7], 3)
        self.rotate([-1,-100,3,99], 2)

# sol = Solution()
# sol.test()
# @lc code=end

