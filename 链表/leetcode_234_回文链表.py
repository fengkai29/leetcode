# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        count = 0
        a = []
        while head != None:
            a.append(head.val)
            head = head.next
        for i in range(len(a)/2):
            if a[i] != a[len(a)-i-1]:
                count = 1
                break
        return count != 1