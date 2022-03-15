# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 == None:
            return root2
        if root2 == None:
            return root1
        
        res_head = None
        stack = list()
        stack.append((None, None, root1, root2))
        
        while stack:
            parent, dirt, cur1, cur2 = stack.pop()
            
            if parent == None:
                parent = TreeNode(cur1.val + cur2.val)
                res_head = parent
                stack.append((parent, "right", cur1.right, cur2.right))
                stack.append((parent, "left", cur1.left, cur2.left))
                continue

            if cur1 == None and cur2 == None:
                continue

            if cur1 != None and cur2 == None:
                node = TreeNode(cur1.val)
                if dirt == "left":
                    parent.left = node
                else:
                    parent.right = node
                stack.append((node, "right", cur1.right, None))
                stack.append((node, "left", cur1.left, None))
            elif cur2 != None and cur1 == None:
                node = TreeNode(cur2.val)
                if dirt == "left":
                    parent.left = node
                else:
                    parent.right = node
                stack.append((node, "right", None, cur2.right))
                stack.append((node, "left", None, cur2.left))
            else:
                node = TreeNode(cur1.val + cur2.val)
                if dirt == "left":
                    parent.left = node
                else:
                    parent.right = node
                stack.append((node, "right", cur1.right, cur2.right))
                stack.append((node, "left", cur1.left, cur2.left))
        
        return res_head