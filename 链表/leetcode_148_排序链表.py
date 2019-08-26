# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        a = []
        while head != None:
            m = head.val
            a.append(m)
            head = head.next
        a.sort()
        count = temp = ListNode(a[0])
        del a[0]
        while a != []:
            temp.next = ListNode(a[0])
            temp = temp.next
            del a[0]
        return count