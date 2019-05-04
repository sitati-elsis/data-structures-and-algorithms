class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.heap = []
    def enqueue(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        index = len(self.heap) - 1
        while index > 0:
            parent_index = int((index - 1)/2)
            parent_node = self.heap[parent_index]
            child_node = self.heap[index]
            if parent_node.value <= child_node.value:
                break
            parent
