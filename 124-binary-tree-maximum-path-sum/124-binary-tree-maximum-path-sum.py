# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs_path(root):
            if root == None:
                return float('-inf'), float('-inf')
            
            left_max, left_path_max = dfs_path(root.left)
            right_max, right_path_max = dfs_path(root.right)
            #print(root.val)
            #print("Left Side: {}, Left Side Path: {}".format(left_max, left_path_max))
            #print("Right Side: {}, Right Side Path: {}".format(right_max, right_path_max))
            #print()
            
            node_max = max(left_max, right_max, left_path_max + root.val, right_path_max + root.val, left_path_max + root.val + right_path_max, root.val)
            path_max = max(left_path_max + root.val, right_path_max + root.val, root.val)
            
            return node_max, path_max
        
        max_val, path_max = dfs_path(root)
        return max_val
        