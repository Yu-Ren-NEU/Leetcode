#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 对于p和q是否是同一棵树, 可以转换成检查
        # 1. p的值和q的值是否相等
        # 2. p的左子树和q的左子树是否相等
        # 3. p的右子树和q的右子树是否相等
        # 以上三个情况同时满足, 才可认为p和q是同一颗树
        
        val_matched = False
        if p and not q: return False
        elif not p and q: return False
        elif not p and not q: return True
        else:
            val_matched = True if p.val == q.val else False
            if not val_matched: return False

        left_matched = False

        if p.left and not q.left: return False
        elif not p.left and q.left: return False
        elif not p.left and q.left: left_matched = True
        else:
            left_matched = self.isSameTree(p.left, q.left)
            if not left_matched: return False

        right_matched = False
        if p.right and not q.right: return False
        elif not p.right and q.right: return False
        elif not p.right and not q.right: right_matched = True
        else:
            right_matched = self.isSameTree(p.right, q.right) 
            if not right_matched: return False
        
        return val_matched and left_matched and right_matched

# @lc code=end

