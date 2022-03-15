# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insertion(root, val):
            if root.val > val.val:
                if root.left == None:
                    root.left = val
                else:
                    insertion(root.left, val)
            else:
                if root.right == None:
                    root.right = val
                else:
                    insertion(root.right, val)
        
        if root == None:
            return TreeNode(val)
        
        insertion(root, TreeNode(val))
        return root
            