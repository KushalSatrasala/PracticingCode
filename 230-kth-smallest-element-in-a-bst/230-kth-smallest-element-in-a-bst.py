# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 1
        stack = list()
        stack.append((root, False))
        
        while stack:
            node, visited = stack.pop()
            if node == None:
                continue
            if visited is False:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
            else:
                if i == k:
                    return node.val
                i += 1
                