class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root = None
    
    def add_node(self, value):
        current = self.root
        if not current:
            self.root = Node(value)
        while current:
            if value > current.value:
                if not current.right_child:
                    current.right_child = Node(value)
                    break
                else:
                    current = current.right_child
            else:
                if not current.left_child:
                    current.left_child = Node(value)
                    break
                else:
                    current = current.left_child

    def bsf(self):
        to_be_visited = []
        visited = []
        node = self.root
        to_be_visited.append(node)
        while to_be_visited:
            node = to_be_visited.pop(0)
            visited.append(node.value)
            if node.left_child:
                to_be_visited.append(node.left_child)
            if node.right_child:
                to_be_visited.append(node.right_child)

        return visited

tree = Tree()
tree.add_node(45)
print(tree.root.value)
tree.add_node(55)
tree.add_node(35)
tree.add_node(33)
tree.add_node(48)
tree.add_node(23)

