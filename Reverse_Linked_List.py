# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:

        # prev = None
        # s=None
        # while head:
        #     s=head.next
        #     head.next=prev
        #     prev=head
        #     head=s
        # print(prev)
        # return prev

        
        if not head:
            return prev
        next_node = head.next
        head.next = prev
        return self.reverseList(next_node, head)


        


