#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: [], m: int, nums2: [], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 将nums2的内容合并到nums1中去
        # 注意这里不能直接insert, 需要将相对应位置的值改变
        
        left_idx = 0
        right_idx = 0
        left_max = m
        right_max = n
        while(left_idx <= left_max and right_idx <= right_max):
            # 对于nums1来说, 只要找到比当前nums2的元素稍微大的位置即可
            if nums1[left_idx] >= nums2[right_idx]:
                nums1[left_idx-1] = nums2[right_idx]
                right_idx += 1
                left_idx +=1
            elif nums1[left_idx] < nums2[right_idx]:
                # 这时找到一个比nums2大的元素,
                # 腾空间给nums2
                nums1[left_idx-1] = nums1[left_idx]
                left_idx += 1
            
        # ! nums2还有未存进nums1的内容
        idx = m
        if right_idx < right_max:
            nums1[left_idx-1] = nums2[right_idx]
            right_idx += 1
            left_idx += 1

        return nums1

        pass
    def test(self):
        print(self.merge([1,0,0,0,0,0], 1, [2,0,0], 1))
        pass

sol = Solution()
sol.test()

# @lc code=end

