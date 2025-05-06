import math

# Create a binary tree as a list
tree = [node for node in range(1, 4)]  # Example tree: [1, 2, 3]

# Function to calculate the number of levels in a binary tree
def calculate_levels(tree):
    if len(tree) == 0:
        return 0
    return math.floor(math.log2(len(tree))) + 1

# Functions to get child and parent indices in a binary tree
def get_left_child(index):
    return 2 * index + 1

def get_right_child(index):
    return 2 * index + 2

def get_parent(index):
    return (index - 1) // 2

# Example usage of child and parent functions
root_index = 0
left_child_index = get_left_child(root_index)
right_child_index = get_right_child(root_index)

print("Left child of root:", tree[left_child_index])
print("Right child of root:", tree[right_child_index])
print("Value of root:", tree[root_index])
print("Number of levels:", calculate_levels(tree))


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

#lista [3,5,7,10,20]
root = Node(10)

root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)

print("Wartość korzenia:", root.value)
print("Wartość lewego dziecka:", root.left.value)
print("Wartość prawego dziecka:", root.right.value)

