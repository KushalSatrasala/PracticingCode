# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        queue = list()
        cur_sum = None
        queue.append(root)
        
        while queue:
            cur_val = 0
            new_queue = list()
            
            for node in queue:
                if not node:
                    continue
                cur_val += node.val
                if node.left:
                    new_queue.append(node.left)    
                if node.right:
                    new_queue.append(node.right)
            
            queue = new_queue
        
        return cur_val
            