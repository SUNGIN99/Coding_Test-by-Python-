class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode('1')
S_Node = head
S_Node.next = ListNode('2'); S_Node = S_Node.next
S_Node.next = ListNode('3'); S_Node = S_Node.next
S_Node.next = ListNode('4'); S_Node = S_Node.next
S_Node.next = ListNode('5'); S_Node = S_Node.next

def reverseList_1(head: ListNode) -> ListNode:

    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)

def printNode(head: ListNode):
    node = head
    while node:
        print(f'{node.val}', end = ' -> ')
        node = node.next
    print('None', end='')
    print()

def reverseList_2(head: ListNode) -> ListNode:
    node, prev = head, None

    print('start', end=' = ')
    printNode(node)
    print()

    while node:
        print(f'cur_node : {node.val})')

        next, node.next = node.next, prev
        print('next: ', end=''); printNode(next)
        print('node: ', end=''); printNode(node)

        prev, node = node, next
        print('prev: ', end=''); printNode(prev)
        print('node: ', end='');printNode(node)

        print()

    return prev
reverseList_2(head)