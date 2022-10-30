from sys import maxsize


class MyCircularDeque:

    class Node:
        def __init__(self, n):
            self.value = n
            self.left = None
            self.right = None

    def __init__ (self, k): # 데크 사이즈를 k로 지정하는 생성자
        self.maxSize = k
        self.curSize = 0
        self.head : self.Node = None
        self.tail : self.Node = None


    def insertFront(self, n : int): # 데크 처음에 아이템을 추가하고 성공할 경우 true를 리턴
        if self.curSize != self.maxSize:
            node = self.Node(n)
            node.left, node.right = None, None
            if self.head is not None:
                node.right = self.head
                self.head.left = node
                self.head = node

            else:
                self.tail = node
                self.head = node

            self.curSize += 1
            return True

        else:
            return False


    def insertLast(self, n : int): # 데크 마지막에 아이템을 추가하고 성공할 경우 true를 리턴
        if self.curSize != self.maxSize:
            node = self.Node(n)
            node.left, node.right = None, None
            if self.tail is not None:
                node.left = self.tail
                self.tail.right = node
                self.tail = node

            else:
                self.head = node
                self.tail = node

            self.curSize += 1
            return True

        else:
            return False

    def deleteFront(self): # 데크 처음에 아이템을 삭제하고 성공할 경우 true를 리턴
        if self.head is not None:
            pre_head = self.head
            
            self.head = self.head.right
            self.head.left = None

            self.curSize -= 1

            del pre_head
            return True
        else:
            return False


    def deleteLast(self): # 데크 마지막에 아이템을 삭제하고 성공할 경우 true를 리턴
        if self.tail is not None:
            pre_tail = self.tail

            self.tail = self.tail.left
            #self.tail.right = None

            self.curSize -= 1

            del pre_tail
            return True
        else:
            return False


    def getFront(self): # 데크의 첫 번째 아이템을 가져온다. 데크가 비어있다면 -1을 리턴
        return -1 if self.head is None else self.head.value

    def getRear(self): # 데크의 마지막 번째 아이템을 가져온다. 데크가 비어있다면 -1을 리턴
        return -1 if self.tail is None else self.tail.value

    def isEmpty(self): # 데크가 비어있는지 여부를 판별
        return self.head is None 

    def isFull(self): # 데크가 가득 차 있는지 여부를 판별
        return self.curSize == self.maxSize


class MyCircularDeque1:
    class Node:
        def __init__(self, n):
            self.value = n
            self.left = None
            self.right = None

    def __init__(self, k: int):
        self.head, self.tail = self.Node(None), self.Node(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: Node, new: Node):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: Node):
        n = node.right.right
        node.right = n
        n.left = node 

    def insertFront(self, value: int) -> bool :
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, self.Node(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, self.Node(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.value if self.len else -1
        
    def getRear(self) -> int:
        return self.tail.left.value if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
    

dq1 = MyCircularDeque(5)
dq2 = MyCircularDeque1(5)

dq1.insertFront(1)
dq1.insertFront(2)
dq1.insertFront(3)

'''
while(True):
    if(dq1.isEmpty()):
        break


    print(dq1.getRear())
    dq1.deleteLast()
'''
print(dq1.isEmpty())
print(dq1.getRear())
print(dq1.deleteLast())
print(dq1.getRear())
print(dq1.deleteLast())
print(dq1.deleteLast())
print(dq1.getRear())
print(dq1.getFront())
print(dq1.isEmpty())