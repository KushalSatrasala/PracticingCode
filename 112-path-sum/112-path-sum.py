# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = list()
        stack.append((root, 0))
        
        while stack:
            node, sum_val = stack.pop()
            
            if node == None:
                continue
            
            if node.left == None and node.right == None and ((sum_val + node.val) == targetSum):
                return True
            
            stack.append((node.right, sum_val + node.val))
            stack.append((node.left, sum_val + node.val))
        
        return False
        