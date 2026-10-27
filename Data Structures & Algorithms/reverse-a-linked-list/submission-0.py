# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new_head= None
        while curr:
            
            new_node = ListNode(val=curr.val, next= new_head)
            new_head=new_node
            curr = curr.next
        return new_head

        
