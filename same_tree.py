# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time Complexity: O(N).

        # Space Complexity:
        #     •	Best Case (Trees Differ Early): If the trees differ near the root, the recursion terminates early, using O(1) space.
        #     •	Worst Case (Identical Trees):
        #     •	If the trees are completely skewed (like linked lists), the recursion depth is O(N).
        #     •	If the trees are balanced, the recursion depth is O(\log N).
        if p and q:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val
        elif p and not q:
            return False
        elif not p and q:
            return False
        else:
            return True
        
