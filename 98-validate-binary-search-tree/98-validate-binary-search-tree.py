# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = list()
        stack.append((root, False))
        prev = None
        
        while stack:
            node, visited = stack.pop()
            if node == None:
                continue

            if not visited:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
            else:
                print(prev, node.val)
                if prev != None and prev >= node.val:
                    return False
                prev = node.val
        
        return True
            
                