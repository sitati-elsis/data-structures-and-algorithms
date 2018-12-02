class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None 


class LinkedList:
    def __init__(self):
        self.head = None

    def print_nodes(self):
        node = self.head
        if not node:
            print('There is no item in the list')

        while node:
            print(node.data)
            node = node.next_node

    def list_length(self):
        count = 0
        node = self.head
        if not node:
            print("list is empty")
        while node:
            count+=1
            node = node.next_node
        return count


    def insert_at_begining(self, new_node):
        head_node = self.head
        self.head = new_node
        new_node.next_node = head_node

    def insert_at_the_end(self, new_node):
        node = self.head
        if not node:
            self.head = new_node

        while node:
            if node.next_node is None:
                break
            node = node.next_node
        node.next_node = new_node

    def insert_at_postion(new_node, position):
        if position < 0 or position > self.list_length():
            print("invalid position")
        elif position == 0:
            self.insert_at_begining(new_node)
        if postion 


first_node = Node(8)
linked_list =  LinkedList()
linked_list.insert_at_begining(first_node)
second_node = Node(15)
linked_list.insert_at_begining(second_node)
third_node = Node(33)
node_four = Node(29)
node_five = Node(32)
node_six = Node(56)
linked_list.insert_at_begining(third_node)
linked_list.insert_at_the_end(node_four)
linked_list.insert_at_the_end(node_five)
linked_list.insert_at_the_end(node_six)
linked_list.print_nodes()
print(linked_list.list_length())