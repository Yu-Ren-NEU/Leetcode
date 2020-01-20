#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 解法1: 直接把所有的值都整合起来统一去重, 然后从小到大生成ListNode
        # 解法2: 因为是有序的链表, 所以可以从链头开始遍历往后检查达到去重的目的, 注意链表操作

        # FUCK: 注意head为空的情况
        if not head: return head

        currNode = head
        nextNode = head.next

        while (nextNode):
            if currNode.val == nextNode.val:
                tempNode = currNode
                while (tempNode.val == nextNode.val):
                    if not nextNode.next: break
                    nextNode = nextNode.next
                # ! 注意边界判断
                # ! 可能是链表到头了, 此时nextNode为最后一个结点
                if not nextNode.next:
                    if nextNode.val == tempNode.val:
                        currNode.next = None
                        nextNode = None
                    else:
                        currNode.next = nextNode
                        nextNode.next = None
                else:
                    # 此时并非链表到头, 而是curr和next不相等的情况
                    # 将链表连接起来
                    currNode.next = nextNode
                    nextNode = currNode.next
            else:
                # 进入下一个ListNode
                currNode = nextNode
                nextNode = currNode.next        
        
        return head   
    def test(self):
        pass

sol = Solution()
sol.test()

# @lc code=end

