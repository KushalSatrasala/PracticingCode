# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def find_elem(root, val, node):
            if root == None:
                return False
            elif root.val == val and root != node:
                return True
            elif root.val > val:
                return find_elem(root.left, val, node)
            else:
                return find_elem(root.right, val, node)
        
        stack = list()
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if cur_node == None:
                continue
            target = k - cur_node.val
            print(target)
            if find_elem(root, target, cur_node):
                return True
            stack.append(cur_node.left)
            stack.append(cur_node.right)
        
        return False
        
            
        