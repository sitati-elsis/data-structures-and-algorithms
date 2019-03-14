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

    def insert_at_position(self, new_node, position):
        if position < 0 or position > self.list_length():
            print("invalid position")
        if position == 0:
            self.insert_at_begining(new_node)

        count = 0
        node = self.head
        while node:
            count += 1
            if count == position:
                 new_node.next_node = node.next_node
                 node.next_node = new_node
                 break
            node = node.next_node

    def delete_end_node(self):
        node = self.head
        count = 0
        while node:
            count += 1
            previous_node = node
            if count == self.list_length() - 1:
                previous_node.next_node = None
                break
            # print(f"the previous node is now {node.data}")
            node = node.next_node

    def delete_at_position(self, position):
        count = 0 
        node = self.head
        while node:
            count += 1
            if count == position:
                current_node = node
                new_node = node.next_node.next_node
                current_node.next_node = new_node
                break

            node = node.next_node



            

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
node_seven = Node(77)
node_eight = Node(88)
linked_list.insert_at_position(node_seven, 5)
linked_list.insert_at_position(node_eight, 7)
linked_list.print_nodes()
print(linked_list.list_length())
# linked_list.delete_end_node()
linked_list.delete_at_position(2)
print("new nodes follow below")
linked_list.print_nodes()
print(linked_list.list_length())





