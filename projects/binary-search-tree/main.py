from bst import BSTNode

tree = BSTNode()

nums = [5, 3, 6, 7, 4, 9, 12]
for num in nums:
    tree.insert(num)

print(tree.values)
print(tree.weights)

print(tree.find(7))
print(tree.find(8))
