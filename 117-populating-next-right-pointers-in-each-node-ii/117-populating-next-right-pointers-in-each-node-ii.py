"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = list()
        queue.append(root)
        prev = None
        
        while queue:
            next_queue = list()
            prev = None
            for node in queue:
                if prev:
                    prev.next = node

                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                prev = node
            
            queue = next_queue
        
        return root