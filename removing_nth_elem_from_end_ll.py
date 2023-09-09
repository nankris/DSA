
# Below is a leetcode question, in the solution i have demonstrated two approches

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Approach 1
        # Two pointer approach
        fast_pointer = head
        slow_pointer = head
        for i in range(n):
            fast_pointer = fast_pointer.next
        
        # This logic is for the case where n is equal to lenth of linked list, then we just remove head
        if fast_pointer == None:
            return head.next

        while fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        
        slow_pointer.next = slow_pointer.next.next
        return head

        # Approach 2
        # first iterate and get the length after then simplay remove the len-nth node
        current_node = head
        if head is None:
            return None
        lent = 0
        while current_node:
            lent += 1
            current_node = current_node.next

        fresh_iter = head
        # This logic is for the case where n is equal to lenth of linked list, then we just remove head
        if lent-n == 0:
            return head.next
        
        for i in range(lent-n):
            prev = fresh_iter
            fresh_iter = fresh_iter.next
        prev.next = prev.next.next
        return head    


