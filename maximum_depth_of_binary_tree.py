# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # •	Time Complexity: O(N) (each node is processed once).
        # •	Space Complexity:
        # •	Worst case (skewed tree): O(N) (recursion stack grows to N).
        # •	Best case (balanced tree): O(log N) (recursion stack grows to log N).

        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
