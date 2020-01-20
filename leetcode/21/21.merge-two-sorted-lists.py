#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
# Author: Liu Song

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 简单粗暴
        # 每次从两个list中取最小的那个. 
        # 然后两个list有两个索引, 取了一个元素就索引加一

        
        resNode = ListNode(0)
        result = resNode

        leftNode = l1
        rightNode = l2

        while(leftNode and rightNode):
            if leftNode.val < rightNode.val: 
                resNode.next = ListNode(leftNode.val)
                resNode = resNode.next

                leftNode = leftNode.next
            elif leftNode.val == rightNode.val:
                resNode.next = ListNode(leftNode.val)
                resNode = resNode.next

                resNode.next = ListNode(rightNode.val)
                resNode = resNode.next
                
                leftNode = leftNode.next
                rightNode = rightNode.next
            else:
                resNode.next = ListNode(rightNode.val)
                resNode = resNode.next

                rightNode = rightNode.next
        # 判断l1是否有剩余
        if leftNode:
            while(leftNode):
                resNode.next = ListNode(leftNode.val)
                resNode = resNode.next
                
                leftNode = leftNode.next

        # 判断l2是否有剩余
        if rightNode:
            while(rightNode):
                resNode.next = ListNode(rightNode.val)
                resNode = resNode.next

                rightNode = rightNode.next

        return result.next
# @lc code=end

