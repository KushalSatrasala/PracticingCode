# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt_head = None
        lt_tail = None
        gt_head = None
        gt_tail = None
        res_head = None
        
        cur_node = head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = None
            if cur_node.val < x:
                if lt_head == None:
                    lt_head = cur_node
                    lt_tail = cur_node
                else:
                    lt_tail.next = cur_node
                    lt_tail = cur_node
            elif cur_node.val >= x:
                if gt_head == None:
                    gt_head = cur_node
                    gt_tail = cur_node
                else:
                    gt_tail.next = cur_node
                    gt_tail = cur_node
            cur_node = next_node
    
        if lt_head:
            res_head = lt_head
            if gt_head:
                lt_tail.next = gt_head
        if not res_head:
            res_head = gt_head
        
        return res_head
        
        