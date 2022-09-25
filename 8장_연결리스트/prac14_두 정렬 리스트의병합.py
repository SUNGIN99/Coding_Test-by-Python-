class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head1 = ListNode('1')
nums1 = head1
nums1.next = ListNode('2'); nums1 = nums1.next
nums1.next = ListNode('4');

head2 = ListNode('1')
nums2 = head2
nums2.next = ListNode('3'); nums2 = nums2.next
nums2.next = ListNode('4');

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if(not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1