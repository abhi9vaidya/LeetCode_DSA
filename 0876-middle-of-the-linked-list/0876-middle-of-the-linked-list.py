# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        if head.next == None:
                return head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast==None or fast.next==None:
                return slow
            