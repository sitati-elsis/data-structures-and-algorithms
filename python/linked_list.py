class Node():
    def __init__(self, data):
        self.next_node = None
        self.data = data


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    # adding a node to the tail of the linked list
    def add(self, node):
        new_node = Node(node)
        # incase we already have a node in the linked list
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node

        # incase we do not have a node in the linked list
        else:
            self.head = new_node
            self.tail = new_node
        # increase the size of the list by one
        self.size += 1

    def add_at(self, node, index):
        new_node = Node(node)
        # keep track of previous node
        previous_node = None
        current_node = self.head
        i = 0
        while i < index and current_node.next_node:
            previous_node = current_node
            current_node = current_node.next_node
            i += 1

        if i == index:
            previous_node.next_node = new_node
            new_node.next_node =   current_node
            return True
        else:
            # list not long enough for the index
            return False

    def remove(self, node):
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.data == node:
                if previous_node:
                    previous_node.next_node = current_node.next_node
                else:
                    self.head = current_node.next_node
                self.size -= 1
                return True
            previous_node = current_node
            current_node = current_node.next_node
        return False
            

    def to_list(self):
        l = []
        current_node = self.head
        while current_node:
            l.append(current_node.data)
            current_node = current_node.next_node
        return l

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
print(l.to_list())
l.add_at("new data", 1)
print(l.to_list())
l.remove("new data")
print(l.to_list())