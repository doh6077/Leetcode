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

        # # The order: 
        # # 0, n, 1, n -1, 2, n-3 ...
        # # first Idea
        # # need to memorize the index of the original head 
        # # Hashmap: iterate through the head until head it none, save index as key and head.val as value 
        # head_hash = {}
        # temp = head
        # index = 0 
        # length = 0 
        # while temp is not None:
        #     head_hash[index] = temp.val
        #     temp = temp.next 
        #     index += 1
        #     length += 1
        # index = 0 
        # count = 1
        # while head is not None: 
        #     res = index % 2 
        #     # if the index is even number 
        #     if res == 0:
        #         head.data = head_hash[index/2]
        #         print("even", index, head.data)
        #     # n, n-1, n-2 when the index is odd 
        #     else:
        #         head.data = head_hash[length - count]
        #         count += 1 
        #         print("odd", index, head.data)

        #     index += 1
        #     head = head.next
        

        # # head_hash = {0:1, 1:2, 2:3, 3:4}
        # # length: 4

        # The order: 
        # 0, n, 1, n -1, 2, n-3 ...
        # first Idea
        # need to memorize the index of the original head 
        # Hashmap: iterate through the head until head it none, save index as key and head.val as value 
        head_hash = {}
        temp = head
        index = 0 
        length = 0 
        while temp is not None:
            head_hash[index] = temp.val
            temp = temp.next 
            index += 1
            length += 1
        index = 0 
        count = 1
        print(head_hash)
        while head is not None: 
            res = index % 2 
            # if the index is even number 
            if res == 0:
                head.val = head_hash[index/2]
                print("even", index, head)
            # n, n-1, n-2 when the index is odd 
            else:
                head.val = head_hash[length - count]
                count += 1 
                print("odd", index, head.val)

            index += 1
            head = head.next
        

        # head_hash = {0:1, 1:2, 2:3, 3:4}
        # length: 4



        