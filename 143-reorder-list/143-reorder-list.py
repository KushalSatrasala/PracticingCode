# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        temp = head
        size = 1
        while(curr.next!=None):
            size+=1
            curr = curr.next
        
        res_list = list()
        curr = head
        i = 0 
        mid = (size // 2)
        while i < mid:
            nxt = curr.next
            curr.next = None
            res_list.append(curr)
            i += 1
            curr = nxt
        
        if size % 2 == 1:
            nxt = curr.next
            curr.next = None
            res_list.append(curr)
            curr = nxt
        
        i -= 1
        while i >= 0:
            nxt = curr.next
            curr.next = None
            if (size % 2 == 0 and i + 1 != mid) or (size % 2 == 1):
                curr.next = res_list[i + 1]
            res_list[i].next = curr
            curr = nxt
            i -= 1

        head = res_list[0]            