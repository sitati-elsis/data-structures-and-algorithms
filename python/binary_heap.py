class MaxBinaryHeap:
    def __init__(self):
        self.heap = []
    def insert_into_heap(self, item):
        self.heap.append(item)
        index = len(self.heap) - 1
        while index > 0:
            parent_index = int((index - 1)/2)
            parent_node = self.heap[parent_index]
            child_node = self.heap[index]
            if parent_node >= child_node:
                break
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

heap1 = MaxBinaryHeap()
heap1.insert_into_heap(41)
heap1.insert_into_heap(39)
heap1.insert_into_heap(33)
heap1.insert_into_heap(18)
heap1.insert_into_heap(27)
heap1.insert_into_heap(12)
heap1.insert_into_heap(55)
print(heap1.heap)