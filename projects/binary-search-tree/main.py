from avl_tree import AVLTree, AVLNode

tree = AVLTree()
x = AVLNode(5)
x.insert(2)
tree.insert(1)
tree.insert(x)

nums = [5, 3, 6, 7, 4, 10, 11, 8, 9, 12, 1, 2]
for num in nums:
    tree.insert(num)
print(tree)
tree.delete(8)
print(tree)
print(tree.values)
