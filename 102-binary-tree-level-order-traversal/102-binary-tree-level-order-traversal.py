# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_val_list = list()
        cur_list = list()
        cur_list.append(root)
        while cur_list:
            next_list = list()
            next_val_list = list()
            for node in cur_list:
                if node == None:
                    continue
                next_val_list.append(node.val)
                next_list.append(node.left)
                next_list.append(node.right)
            
            cur_list = next_list
            if next_val_list:
                res_val_list.append(next_val_list)
        return res_val_list