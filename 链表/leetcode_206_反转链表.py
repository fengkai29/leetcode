# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        a = []
        while head != None:
            a.append(head.val)
            head = head.next
        a.reverse()
        if a == []:
            return None
        else:
            m = ListNode(a[0])
            r = m
            for i in range(1,len(a)):
                r.next = ListNode(a[i])
                r = r.next
            return m