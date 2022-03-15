# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        diff_set = set()        
        stack = list()
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if (k - cur_node.val) in diff_set:
                return True
            diff_set.add(cur_node.val)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        return False