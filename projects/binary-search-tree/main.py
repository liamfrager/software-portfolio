from avl_tree import AVLTree

tree = AVLTree()

nums = [5, 3, 6, 7, 4, 10, 11, 8, 9, 12, 1, 2]
for num in nums:
    tree.insert(num)
    # print(tree)

print(tree)
# print(tree.values)
