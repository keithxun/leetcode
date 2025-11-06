# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dict = {}
        for i in nums:
            dict[i] = i

        ans = ListNode()
        header = ans
        while head != None:
            if head.val in dict:
                head = head.next
            else:
                header.next = ListNode(val=head.val)
                header = header.next
                head = head.next

        return ans.next
