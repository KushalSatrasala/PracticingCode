# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = list()
        res_list = list()   
        stack.append((root, False))
        
        while stack:
            cur, visited = stack.pop()
            if cur == None:
                continue
            if visited:
                res_list.append(cur.val)
                continue
            stack.append((cur, True))
            stack.append((cur.right, False))
            stack.append((cur.left, False))
        return res_list