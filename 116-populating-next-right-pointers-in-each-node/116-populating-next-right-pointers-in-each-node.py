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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur_queue = collections.deque()
        cur_queue.append(root)
        
        while True:
            next_queue = collections.deque()
            prev = None
            while cur_queue:
                cur_node = cur_queue.popleft()
                if not cur_node:
                    continue
                next_queue.append(cur_node.left)
                next_queue.append(cur_node.right)
                if prev:
                    prev.next = cur_node
                prev = cur_node
            
            if not next_queue:
                break
            cur_queue = next_queue
        return root
        