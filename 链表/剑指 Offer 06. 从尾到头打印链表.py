'''
剑指 Offer 06. 从尾到头打印链表
简单

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 
示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
'''

# way1: 栈的思想
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversPrint(self, head):        
        stack = [] # 初始化栈
        while head is not None: # 如果头指针不是空的（说明这个节点存在值哈）
            stack.append(head.val) # 把这个节点的值，append到stack上
            head = head.next # 移动head指针到下一个位置
        return stack[::-1] # 逆序返回list（或者说stack）就好



# way2: 递归

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
class LinkList(object):
    def __init__(self):
        self.head = None
    
    def initList(self, data): # data为list形式
        self.head = ListNode(data[0]) # 创建头节点
        r = self.head # r为指针，指向头结点（这个r指针用来保存（或者说指向）头结点位置的）
        p = self.head # p也为指针，指向头结点（这个p指针后续用来移动的）
        
        for i in data[1:]: # 逐个为data内的数据创建结点，建立链表
            node = ListNode(i) # 创建对应数据的节点
            p.next = node # 将p的下一个指向该node
            p = p.next # 移动p
        return r # 遍历完之后，就返回r，即为链表了


class Solution(object):
    def reversePrint(self, head):
        if head is None:
            return []
        else:
            res = self.reversePrint(head.next)
            res.append(head.val)
            return res


data = [1,3,2]
linklist = LinkList()
linklist = linklist.initList(data) # 创建链表
print(linklist)

s = Solution()
result = s.reversePrint(linklist) # 从尾到头打印链表
print(result)