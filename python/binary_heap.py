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

    def remove_max(self):
        root = self.heap[0]
        last_item = self.heap.pop()
        self.heap[0] = last_item
        print(f"heap is now {self.heap}")
        self.bubble_down()
        return root

    def bubble_down(self):
        index = 0
        while index < len(self.heap):
            print(f"index is {index}")
            left_child_index = (2 * index) + 1
            right_child_index = (2 * index + 2)
            parent = self.heap[index]
            print(f"parent is {parent}")
            children = []
            if left_child_index < len(self.heap):
                left_child = self.heap[left_child_index]
                print(f"left child is {left_child}")
                children.append(left_child)
            if right_child_index < len(self.heap):
                right_child = self.heap[right_child_index]
                print(f"right child is {right_child}")
                children.append(right_child)
            print(f"chidlren are {children}")
            if not children:
                break
            greatest_child = max(children)
            print(f"greatest child is {greatest_child}")
            if parent >= greatest_child:
                break
            print(f"we are lookin for {greatest_child} in {self.heap} ")
            index_of_greatest = self.heap.index(greatest_child)
            print(f"index of greatest child is {index_of_greatest}")
            self.heap[index] = greatest_child
            self.heap[index_of_greatest] = parent
            print(f"heap now looks like {self.heap}")
            index  = index_of_greatest
            

heap1 = MaxBinaryHeap()
heap1.insert_into_heap(41)
heap1.insert_into_heap(39)
heap1.insert_into_heap(33)
heap1.insert_into_heap(18)
heap1.insert_into_heap(27)
heap1.insert_into_heap(12)
heap1.insert_into_heap(55)
print(heap1.heap)
print(heap1.remove_max())
print(heap1.heap)
print(heap1.remove_max())
print(heap1.heap)
print(heap1.remove_max())
print(heap1.heap)