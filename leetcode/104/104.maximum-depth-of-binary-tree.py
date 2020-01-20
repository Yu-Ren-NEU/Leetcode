#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 问题可以简化为 
        # 一棵树的最大深度, 取决于它的左右两个子树的最大深度

        # 到叶节点了, 叶节点没有子树
        if not root:    return 0

        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)

        max_child_depth = max(left_max_depth, right_max_depth)

        return 1+max_child_depth

# @lc code=end

