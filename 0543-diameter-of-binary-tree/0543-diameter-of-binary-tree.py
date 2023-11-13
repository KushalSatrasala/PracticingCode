# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_lenght = 0

        def travel_tree(cur_node):
            if cur_node == None:
                return 0     
            max_llen = travel_tree(cur_node.left)
            max_rlen = travel_tree(cur_node.right)
            #print(max_llen, max_rlen)
            max_len = max_llen + max_rlen + 1
            
            if max_len > self.max_lenght:
                 self.max_lenght = max_len
            
            return max(max_llen, max_rlen) + 1
        
        travel_tree(root)
        return self.max_lenght - 1
