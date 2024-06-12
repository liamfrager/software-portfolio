from avl_tree import AVLTree, AVLNode

tree = AVLTree()
# x = AVLNode(5)
# x.insert(2)
# tree.insert(1)
# tree.insert(x)

nums = [5, 3, 6, 7, 4, 10, 11, 8, 9, 12, 1, 2]
for num in nums:
    print(num, tree.insert(num))
tree.delete(8)
print(tree)
if tree.delete(4):
    print(tree)
# print(tree.find(10))
# print(tree.values)
