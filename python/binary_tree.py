  class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root = None

    def to_object(self):
        pass

    def add_node(self, value):
        node = self.root
        if not node:
            self.root = Node(value)
            return
        while node:
            if node.value > value :
                //go left
                # if you find a node
                if node.left_child:
                    node = node.left_child
                else:
                    node.left_child = Node(value)
                    break
            else:
                # go right
                if node.right_child:
                    node = node.right_child
                else:
                    node.right_child = new Node(value)
                    break

