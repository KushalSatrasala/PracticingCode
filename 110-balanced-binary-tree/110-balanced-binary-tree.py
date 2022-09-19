# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs_travel(cur_node):
            if cur_node == None:
                return 0, True
            left, lflag = dfs_travel(cur_node.left)
            right, rflag = dfs_travel(cur_node.right)
            if (not lflag or not rflag) or abs(left - right) > 1:
                return -1, False
            return max(left,right) + 1, True
        
        return dfs_travel(root)[1]