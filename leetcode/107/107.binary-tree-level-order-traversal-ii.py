#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
# Author: Liu Song

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # 使用广度优先遍历算法
        # 将父节点存入队列, 然后父节点出队, 将左右子节点存入队列
        # 再对左右子节点做相同的事情即可

        from collections import deque

        if not root: return []
        
        depth = 0
        result = []
        queue = deque([(root, depth)])
       
        while(queue):
            curr, depth = queue.popleft()
            if curr:
                if len(result) < depth+1:
                    # 创建空间
                    result.insert(0, [])
                queue.append([curr.left, depth+1])
                queue.append([curr.right, depth+1])            
                result[-(depth+1)].append(curr.val)
        return result

# @lc code=end

