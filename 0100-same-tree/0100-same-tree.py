# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []
        stack.append((p, q))

        while stack:
            l1, l2 = stack.pop()

            if l1 is None and l2 != None:
                return False
            if l2 is None and l1 != None:
                return False
            if l1 is None:
                continue
            if l1.val != l2.val:
                return False
            
            stack.append((l1.left, l2.left))
            stack.append((l1.right, l2.right))
        
        return True