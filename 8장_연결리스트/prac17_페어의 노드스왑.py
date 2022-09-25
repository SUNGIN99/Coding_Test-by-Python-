class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head1 = ListNode('1')
nums1 = head1
nums1.next = ListNode('2'); nums1 = nums1.next;
nums1.next = ListNode('3'); nums1 = nums1.next;
nums1.next = ListNode('4')


def swapPairs(self, head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head

    while head and head.next:
        # b가 a(head)를 갈키ㅣ도록 할당
        b = head.next
        head.next = b.next
        b.next= head

        prev.next = b

        head = head.next
        prev = prev.next.next

    return root.next