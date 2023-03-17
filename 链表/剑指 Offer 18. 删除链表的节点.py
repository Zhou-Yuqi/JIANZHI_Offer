'''
题目
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
  剑指Offer 18. 删除链表的节点

说明：
题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def deleteNode(self, head, value):
        r = head
        p = head

        if p.val == value: # 先处理第一个节点
          return p.next

        while p and p.next is not None:
            if p.next.val == value:
                p.next = p.next.next # 跳过重复值
            p = p.next # 移动p到下一个位置

        return r
    
  #  def deleteNode(self, head: ListNode, val: int) -> ListNode:

  #       # maintain an unchanging reference to node ahead of the return node.
  #       reserve_head = head

  #       if head.val == val:      # The first link is matched
  #           return head.next

  #       while head and head.next:
  #           if head.next.val == val:
  #               head.next = head.next.next
  #           head = head.next

  #       return reserve_head