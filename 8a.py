from functools import reduce

# Used to implement the tree datastructure
class Node:

    def __init__(self):
        self.children = []
        self.metadata = []

    def add_child(self, child):
        self.children.append(child)
    
    def add_metadata(self, value: int):
        self.metadata.append(value)
              
# Problem solution

input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
inputs = input.split(' ')

def parse_nodes(numbers: []):
    num_children = int(numbers.pop(0))
    num_metadata = int(numbers.pop(0))
    node = Node()
    for i in range(0, num_children):
        numbers, child = parse_nodes(numbers = numbers)
        node.add_child(child)
    for j in range(0, num_metadata):
        node.add_metadata(int(numbers.pop(0)))
    return numbers, node

def sum_list(values: list):
    return reduce((lambda x,y: x + y), values)

a, root = parse_nodes(inputs)
sum = sum_list(root.metadata)
nodes = root.children
while nodes:
    node = nodes.pop(0)
    nodes = nodes + node.children if node.children else nodes
    sum = sum + sum_list(node.metadata) if node.metadata else sum
print(sum)