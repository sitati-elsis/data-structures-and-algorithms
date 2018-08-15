class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # when root is empty
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            # if current node doesn't have a left child
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)

            else:
                self._insert(value, cur_node.left_child)

        elif value > cur_node.value:
            # if the value is greater than current node value
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)

        # if value euquals current node value
        else:
            print("Value already in tree") 

    def print_tree(self):
        if self.root != None: 
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.left_child)

def fill_tree(tree, num_elements=100, max_int=1000):
    from random import randint
    for _ in list(range(num_elements)):
        cur_element = randint(0, max_int)
        tree.insert(cur_element)
    return tree
    
tree = BinarySearchTree()
tree = fill_tree(tree)
tree.print_tree()