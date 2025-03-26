# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time complexity: O(N), where N is the number of nodes in the tree.

        # Space Complexity:
        #     •	Best Case (Balanced Tree):
        #     •	The recursive call stack goes O(log N) deep for a balanced tree.
        #     •	So, Space Complexity = O(log N).
        
        #     •	Worst Case (Skewed Tree, like a linked list):
        #     •	The recursion calls go N levels deep (one per node).
        #     •	So, Space Complexity = O(N).
        if not root:
            return root
        
        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp

        return root


        
