# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy_head = dummy

        while list1 != None and list2 != None :
            if list1.val <= list2.val:
                #hold the rest of the linked list
                temp_list1 = list1.next
                
                #add the node to the dummy liked list
                dummy.next = list1

                #moves the linked list to the next node
                list1 = temp_list1

                #moves the dummy linked list to the next node
                dummy = dummy.next
            else:
                #hold the rest of the linked list
                temp_list2 = list2.next
                
                #add the node to the dummy liked list
                dummy.next = list2

                #moves the linked list to the next node
                list2 = temp_list2

                #moves the dummy linked list to the next node
                dummy = dummy.next

        #adds the rest of the list to the dummy list
        if list1 == None:
            dummy.next = list2
        else:
            dummy.next = list1

        return dummy_head.next
