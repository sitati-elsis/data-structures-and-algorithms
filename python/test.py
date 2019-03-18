class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node:
                if not node.next:
                    break
                node = node.next
            node.next = new_node
    
    def insert_beginnig(self, new_node):
        if not self.head:
            self.head = new_node
        node = self.head
        self.head = new_node
        new_node.next = node

    def print(self):
        node = self.head
        if not self.head:
            print("There is nothing in the list")
        else:
            while node:
                print(node.data)
                node = node.next
    
    def list_length(self):
        node = self.head
        count = 0
        if not node:
            return "The node is empty"
        while node:
            count = count + 1
            node = node.next
        
        return count

    def insert_at_position(self, position, new_node):
        if position < 0 or position > self.list_length():
            print("insert valid position")
            return
        if position == 0:
            self.insert_beginnig(new_node)
            return
        node = self.head
        count = 0
        while node:
            if count == position:
                previous_node.next = new_node
                new_node.next = node
                break
            previous_node = node
            node = node.next
     
            count = count + 1
    def delete_last(self):
        node = self.head
        while node:
            previous_node = node
            node = node.next
        del node
        previous_node.next = None
        

            

first_node = Node('one')
linked_list = LinkedList()
linked_list.insert(first_node)
second_node = Node('two')
linked_list.insert(second_node)
third_node = Node('three')
linked_list.insert_beginnig(third_node)
fourth_node = Node('four')
linked_list.insert_at_position(2, fourth_node)
linked_list.delete_last()
linked_list.print()
print(linked_list.list_length())
