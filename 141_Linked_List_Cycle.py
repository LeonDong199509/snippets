# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Floyd’s Cycle Detection Algorithm (a.k.a. Tortoise and Hare 🐢🐇).
        # 	•	Use two pointers:
        # •	slow moves one step at a time.
        # •	fast moves two steps at a time.
        # •	If there’s a cycle, fast and slow will eventually meet.
        # •	If fast reaches the end (None), there’s no cycle.
        # WHY?
    #     	•	Since the list is finite and circular, this is guaranteed to happen — think of two runners on a circular track:
	# •	The faster runner (fast) will eventually catch up with the slower runner (slow) no matter where they started.

        # Time O(n), Space O(1)
        slow = head
        fast = head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        
        return False


        
