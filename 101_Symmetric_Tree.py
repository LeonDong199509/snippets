# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Recursion    Write a helper function isMirror(t1, t2) that:
        # •	Returns True if t1 and t2 are mirror images.
        # •	Check:
        # •	Both nodes are None → symmetric.
        # •	One is None, the other isn’t → not symmetric.
        # •	Values are equal and
        # •	isMirror(t1.left, t2.right) and
        # •	isMirror(t1.right, t2.left)
        # Time O(n), Space O(h)
        # def isMirror(t1, t2):
        #     if t1 is None and t2 is None:
        #         return True
        #     elif t1 is None or t2 is None:
        #         return False
        #     else:
        #         if t1.val != t2.val:
        #             return False
        #         else:
        #             return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        # if root is None:
        #     return True
        # else:
        #     return isMirror(root.left, root.right)
    
        # Iteration Idea:
        # •	Use a queue to perform level-order traversal.
        # •	Compare nodes in mirrored positions.
        # •	Enqueue children in mirrored order.
        from collections import deque
        queue = deque([(root, root)])
        while queue:
            t1, t2 = queue.popleft()
            if not t1 and not t2:
                continue
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        return True
