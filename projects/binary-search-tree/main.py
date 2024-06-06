from bst import BSTNode

tree = BSTNode()

nums = [5, 3, 6, 7, 4, 10, 11, 8, 9]
# nums = [5, 3, 6, 7, 4, 10]
for num in nums:
    tree.insert(num)

print(tree)

print(tree.values)

print(tree.find(7))
print(tree.find(8))

print(tree)
