# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = list()
        q_stack = list()
        
        p_stack.append(p)
        q_stack.append(q)
        
        while p_stack and q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()
            
            if p_node and q_node and p_node.val == q_node.val:
                p_stack.append(p_node.left)
                p_stack.append(p_node.right)
                q_stack.append(q_node.left)
                q_stack.append(q_node.right)
                continue
            
            if (p_node is None and q_node is not None) or (q_node is None and p_node is not None):
                return False
            
            if p_node is None and q_node is None:
                continue
            
            if p_node.val != q_node.val:
                return False
        
        if len(p_stack) != 0 or len(q_stack) != 0:
            return False
        
        return True
                