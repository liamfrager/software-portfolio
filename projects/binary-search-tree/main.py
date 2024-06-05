from bst import BSTNode

tree = BSTNode()

nums = [5, 3, 6, 7, 4, 10, 11, 8, 9]
for num in nums:
    print(num)
    tree.insert(num)

print(tree.values)
print(tree.weights)

print(tree.find(7))
print(tree.find(8))
