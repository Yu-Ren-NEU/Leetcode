#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 同样用双端队列, 把父节点子节点依次入队. 用BFS算法
        if not root: return 0
        from collections import deque
        depth = 0
        queue = deque([(root, depth)])
        while(queue):
            curr, depth = queue.popleft()
            if curr:
                if not curr.left and not curr.right:
                    return depth+1
                
                queue.append((curr.left, depth+1))
                queue.append((curr.right, depth+1))
        
# @lc code=end

