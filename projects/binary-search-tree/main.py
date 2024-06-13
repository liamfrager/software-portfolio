from avl_tree import AVLTree, AVLNode

tree = AVLTree()
print(tree)

nums = [5, 3, 6, 7, 4, 10, 11, 8, 9, 12, 1, 2]
for num in nums:
    print(num, tree.insert(num))
    print(tree)

print('delete 12', tree if tree.delete(12) else '')
print('delete 8', tree if tree.delete(8) else '')
print('delete 4', tree if tree.delete(4) else '')
print(tree.find(7))

print(tree.values)
