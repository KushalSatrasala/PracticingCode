# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        stack = list()
        stack.append((root.left, root.right))
        
        while stack:
            ltree, rtree = stack.pop()
            if ltree == None and rtree != None:
                return False
            if rtree == None and ltree != None:
                return False
            if ltree == None and rtree == None:
                continue
            if ltree.val != rtree.val:
                return False
            stack.append((ltree.left, rtree.right))
            stack.append((ltree.right, rtree.left))
        
        return True
        