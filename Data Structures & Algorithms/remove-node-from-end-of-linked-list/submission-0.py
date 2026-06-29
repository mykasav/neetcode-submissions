# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Create a dummy node to handle edge cases smoothly
        dummy = ListNode(0)
        dummy.next = head
        
        # Both pointers start at the dummy node
        fast = dummy
        slow = dummy
        
        # 1. Give the fast runner a head start of 'n' steps
        for _ in range(n):
            fast = fast.next
            
        # 2. Move both pointers at the same speed until 'fast' reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # 3. Bypass the target node (The Alice, Bob, Charlie handshake!)
        slow.next = slow.next.next
        
        # Return the actual head of the list
        return dummy.next

            
        