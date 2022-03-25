# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_dict = dict()
        
        cur_node = head
        cur_indx = 0
        
        while cur_node:
            if cur_node not in node_dict:
                node_dict[cur_node] = cur_indx
            else:
                return cur_node
            cur_node = cur_node.next
            cur_indx += 1
        
        return None