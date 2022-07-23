heap = [-9999];

N = int(input());

for i in range(0, N, 1):
    heap.append(int(input()))
    last_node = len(heap)

    if(last_node == 2):
        continue;

    elif(last_node > 2):
        # heap이 루트 노드만 가지고 있지 않을때
        if(heap[last_node] < heap[last_node//2]):
            temp = heap[last_node]
            heap[last_node//2] = heap[last_node]
            heap[last_node] = temp

 #https://www.acmicpc.net/problem/1927
 
def heap_sort():


def heap_input():


def min_heap():
    return heap[1];