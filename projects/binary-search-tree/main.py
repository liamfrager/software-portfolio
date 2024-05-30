from bst import Node

tree = Node()

nums = [5, 3, 6, 7, 3, 9, 12]
for num in nums:
    tree.insert(num)

print(tree.values)
