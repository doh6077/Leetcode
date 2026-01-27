# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head 
        current = prev = dummy
        stop_index = []
        count = 0 
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                continue             
            current = current.next
        
        # current = dummy 

        # for index in stop_index:
        #     for _ in range(index):
                

        
        return dummy.next 
        