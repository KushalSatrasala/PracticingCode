# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        def find_path_node(cur_root, target):
            if cur_root is None:
                return False, list()
            if cur_root.val == target:
                return True, [cur_root.val]
            
            lflag, lt = find_path_node(cur_root.left, target)
            if lflag:
                lt.append(cur_root.val)
                return True, lt
            rflag, rt = find_path_node(cur_root.right, target)
            if rflag:
                rt.append(cur_root.val)
                return True, rt
            
            return False, list()
        
        pflag, p_path = find_path_node(root, p)
        qflag, q_path = find_path_node(root, q)
        
        if p in q_path:
            indx = q_path.index(p)
            return indx
        
        if q in p_path:
            indx = p_path.index(q)
            return indx
        
        i = len(p_path) - 1
        j = len(q_path) - 1
        while p_path[i] == q_path[j]:
            i -= 1
            j -= 1
        return i + j + 2