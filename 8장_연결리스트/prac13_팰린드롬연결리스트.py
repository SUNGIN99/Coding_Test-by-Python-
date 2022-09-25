# 연결 리스트가 팰린드롬 구조인지 판별하라

'''
S1 = list(input().split('->'))
S2 = input().split('->')
print(type(S1))
print(type(S2))

S1 = '1->2'
S2 = '1->2->2->1'
'''

import collections
from typing import Deque, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode('1')
S_Node = head
S_Node.next = ListNode('2'); S_Node = S_Node.next
S_Node.next = ListNode('3'); S_Node = S_Node.next
S_Node.next = ListNode('4'); S_Node = S_Node.next
S_Node.next = ListNode('3'); S_Node = S_Node.next
S_Node.next = ListNode('2'); S_Node = S_Node.next
S_Node.next = ListNode('1')

def isPalindrome_2(head: ListNode) -> bool:
    rev: ListNode = None
    slow = fast = head

    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    return not rev
node = head
while node:
    print(node.val, end='')
    node= node.next
print('\n', isPalindrome_2(head))
node = head
while node:
    print(node.val, end='')
    node= node.next

# 풀이1
def isPalindrome_1(head: ListNode) -> bool:
    q: Deque = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True
