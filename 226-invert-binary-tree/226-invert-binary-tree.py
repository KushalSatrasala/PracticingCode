# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        stack = list()
        stack.append(root)

        while stack:
            node = stack.pop()
            if node == None:
                continue
            
            left = node.left
            right = node.right
            node.left = right
            node.right = left
            stack.append(right)
            stack.append(left)
        return root