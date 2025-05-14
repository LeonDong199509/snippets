# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #     ✅ Algorithm (Recursive Approach):
        # 1.	Use the first value in preorder as the root.
        # 2.	Find that value in the inorder list to split it into left and right subtrees.
        # 3.	Recursively build the left and right subtrees using updated slices of preorder and inorder.
        # 4.	Use a hashmap to store inorder value → index mapping for O(1) lookups.
        # Time O(n), Space O(n)
        inorder_hashmap = {value: index for index, value in enumerate(inorder)}
        self.root_preorder_index = 0

        def helper(left_inorder_index, right_inorder_index):
            if left_inorder_index > right_inorder_index:
                return None
            root_val = preorder[self.root_preorder_index]
            root_inorder_index = inorder_hashmap[root_val]
            root_node = TreeNode(root_val)

            self.root_preorder_index += 1
            root_node.left = helper(left_inorder_index, root_inorder_index-1)
            root_node.right = helper(root_inorder_index+1, right_inorder_index)

            return root_node

        return helper(0, len(preorder)-1)
        
