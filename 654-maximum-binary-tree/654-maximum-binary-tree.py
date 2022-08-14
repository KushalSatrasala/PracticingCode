# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def createTree(nums):
            if len(nums) == 1:
                return TreeNode(nums[0])
            if len(nums) == 0:
                return None
            
            max_val = max(nums)
            max_indx = nums.index(max_val)
            cur_node = TreeNode(max_val)
            
            left = createTree(nums[0:max_indx])
            right = createTree(nums[max_indx + 1:])
            
            cur_node.left = left
            cur_node.right = right
            
            return cur_node
        
        return createTree(nums)
            