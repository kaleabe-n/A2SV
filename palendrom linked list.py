# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        temp = head
        values = []
        while temp is not None:
            values.append(temp.val)
            temp = temp.next
        return True if values == values[::-1] else False
        """
        :type head: ListNode
        :rtype: bool
        """
        
