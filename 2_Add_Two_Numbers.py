# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # Time O(max(m,n)), Space O(max(m,n))
        result = ListNode()
        current_node = result
        carry = 0
        while(l1 or l2 or carry):
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            current_val = total % 10
            current_node.val = current_val
            current_node.next = None

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            carry = total // 10

            if (l1 or l2 or carry):
                new_node = ListNode()
                current_node.next = new_node
                current_node = new_node

        return result

                


        
