from csc148_queue import Queue


class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.
    """

    def __init__(self, data, left=None, right=None):
        """
        Create BinaryTree self with data and children left and right.

        :param BinaryTree self: this binary tree
        :param object data: data of this node
        :param BinaryTree|None left: left child
        :param BinaryTree|None right: right child
        :rtype: None
        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other):
        """
        Return whether BinaryTree self is equivalent to other.

        :param BinaryTree self: this binary tree
        :param Any other: object to check equivalence to self
        :rtype: bool

        >>> BinaryTree(7).__eq__("seven")
        False
        >>> b1 = BinaryTree(7, BinaryTree(5))
        >>> b1.__eq__(BinaryTree(7, BinaryTree(5), None))
        True
        """
        return (type(self) == type(other) and
                self.data == other.data and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self):
        """
        Represent BinaryTree (self) as a string that can be evaluated to
        produce an equivalent BinaryTree.

        :param BinaryTree self: this binary tree
        :rtype: str

        >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
        BinaryTree(1, BinaryTree(2, None, None), BinaryTree(3, None, None))
        """
        return "BinaryTree({}, {}, {})".format(repr(self.data),
                                               repr(self.left),
                                               repr(self.right))

    def __str__(self, indent=""):
        """
        Return a user-friendly string representing BinaryTree (self)
        inorder.  Indent by indent.

        >>> b = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = (self.right.__str__(
            indent + "    ") if self.right else "")
        left_tree = self.left.__str__(indent + "    ") if self.left else ""
        return (right_tree + "{}{}\n".format(indent, str(self.data)) +
                left_tree)

    def __contains__(self, value):
        """
        Return whether tree rooted at node contains value.

        :param BinaryTree self: binary tree to search for value
        :param object value: value to search for
        :rtype: bool

        >>> BinaryTree(5, BinaryTree(7), BinaryTree(9)).__contains__(7)
        True
        """
        return (self.data == value or
                (self.left and value in self.left) or
                (self.right and value in self.right))


def evaluate(b):
    """
    Evaluate the expression rooted at b.  If b is a leaf,
    return its float data.  Otherwise, evaluate b.left and
    b.right and combine them with b.data.

    Assume:  -- b is a non-empty binary tree
             -- interior nodes contain data in {"+", "-", "*", "/"}
             -- interior nodes always have two children
             -- leaves contain float data

     :param BinaryTree b: binary tree representing arithmetic expression
     :rtype: float

    >>> b = BinaryTree(3.0)
    >>> evaluate(b)
    3.0
    >>> b = BinaryTree("*", BinaryTree(3.0), BinaryTree(4.0))
    >>> evaluate(b)
    12.0
    """
    if not (b.left or b.right):
        # t is a leaf
        return b.data
    else:
        # b is an internal node
        return eval(str(evaluate(b.left)) +
                    str(b.data) + str(evaluate(b.right)))


def postorder_visit(t, act):
    """
    Visit BinaryTree t in postorder and act on nodes as you visit.

    :param BinaryTree|None t: binary tree to visit
    :param (BinaryTree)->Any act: function to use on nodes
    :rtype: None

    >>> b = BinaryTree(8)
    >>> b = bst_insert(b, 4)
    >>> b = bst_insert(b, 2)
    >>> b = bst_insert(b, 6)
    >>> b = bst_insert(b, 12)
    >>> b = bst_insert(b, 14)
    >>> b = bst_insert(b, 10)
    >>> def f(node): print(node.data)
    >>> postorder_visit(b, f)
    2
    6
    4
    10
    14
    12
    8
    """
    if t is None:
        # empty tree
        pass
    else:
        # non-empty tree
        postorder_visit(t.left, act)
        postorder_visit(t.right, act)
        act(t)


def inorder_visit(root, act):
    """
    Visit each node of binary tree rooted at root in order and act.

    :param BinaryTree|None root: binary tree to visit
    :param (BinaryTree)->object act: function to execute on visit
    :rtype: None

    >>> b = BinaryTree(8)
    >>> b = bst_insert(b, 4)
    >>> b = bst_insert(b, 2)
    >>> b = bst_insert(b, 6)
    >>> b = bst_insert(b, 12)
    >>> b = bst_insert(b, 14)
    >>> b = bst_insert(b, 10)
    >>> def f(node): print(node.data)
    >>> inorder_visit(b, f)
    2
    4
    6
    8
    10
    12
    14
    """
    if root is None:
        # empty tree
        pass
    else:
        # non-empty tree
        inorder_visit(root.left, act)
        act(root)
        inorder_visit(root.right, act)


def visit_level(t, n, act):
    """
    Visit each node of BinaryTree t at level n and act on it.  Return
    the number of nodes visited visited.

    :param BinaryTree|None t: binary tree to visit
    :param int n: level to visit
    :param (BinaryTree)->Any act: function to execute on nodes at level n
    :rtype: int

    >>> b = BinaryTree(8)
    >>> b = bst_insert(b, 4)
    >>> b = bst_insert(b, 2)
    >>> b = bst_insert(b, 6)
    >>> b = bst_insert(b, 12)
    >>> b = bst_insert(b, 14)
    >>> b = bst_insert(b, 10)
    >>> def f(node): print(node.data)
    >>> visit_level(b, 2, f)
    2
    6
    10
    14
    4
    """
    if t is None:
        # empty tree!
        return 0
    elif n == 0:
        act(t)
        return 1
    else:
        return (visit_level(t.left, n-1, act) +
                visit_level(t.right, n-1, act))


def levelorder_visit(t, act):
    """
    Visit BinaryTree t in level order and act on each node.

    :param BinaryTree|None t: binary tree to visit
    :param (BinaryTree)->Any act: function to use during visit
    :rtype: None

    >>> b = BinaryTree(8)
    >>> b = bst_insert(b, 4)
    >>> b = bst_insert(b, 2)
    >>> b = bst_insert(b, 6)
    >>> b = bst_insert(b, 12)
    >>> b = bst_insert(b, 14)
    >>> b = bst_insert(b, 10)
    >>> def f(node): print(node.data)
    >>> levelorder_visit(b, f)
    8
    4
    12
    2
    6
    10
    14
    """
    # this approach uses iterative deepening
    # visited, n = visit_level(t, 0, act), 0
    # while visited > 0:
    #     n += 1
    #     visited = visit_level(t, n, act)
    #    uses a Queue
    if t is None:
        pass
    else:
        nodes = Queue()
        nodes.add(t)
        while not nodes.is_empty():
            next_node = nodes.remove()
            act(next_node)
            if next_node.left:
                nodes.add(next_node.left)
            if next_node.right:
                nodes.add(next_node.right)

# assume binary search tree order property


def bst_contains(node, value):
    """
    Return whether tree rooted at node contains value.

    Assume node is the root of a Binary Search Tree

    :param BinaryTree|None node: node of a Binary Search Tree
    :param object value: value to search for
    :rtype: bool

    >>> bst_contains(None, 5)
    False
    >>> bst_contains(BinaryTree(7, BinaryTree(5), BinaryTree(9)), 5)
    True
    """
    if node is None:
        # empty tree!
        return False
    elif node.data < value:
        return bst_contains(node.right, value)
    elif node.data > value:
        return bst_contains(node.left, value)
    else:
        return True


def bst_insert(node, data):
    """
    Insert data in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    :param BinaryTree node: root of a binary search tree.
    :param object data: data to insert into BST, if necessary.

    >>> b = BinaryTree(5)
    >>> b1 = bst_insert(b, 3)
    >>> print(b1)
    5
        3
    <BLANKLINE>
    """
    return_node = node
    if not node:
        return_node = BinaryTree(data)
    elif data < node.data:
        node.left = bst_insert(node.left, data)
    elif data > node.data:
        node.right = bst_insert(node.right, data)
    else:  # nothing to do
        pass
    return return_node


def bst_delete(root, data):
    """
    Delete data in BST rooted at root and return True;
    return False if data is not in the tree.

    Assume root is the root of a Binary Search Tree.

    :param BinaryTree root: root of a binary search tree.
    :param object data: data to delete from BST, if exists.

    >>> b = BinaryTree(5)
    >>> b1 = bst_insert(b, 3)
    >>> b2 = bst_insert(b1, 8)
    >>> bst_delete(b2, 3)
    True
    >>> print(b2)
        8
    5
    <BLANKLINE>
    """
    parent = None
    current = root
    while current is not None and current.data != data:
        if data < current.data:
            parent = current
            current = current.left
        elif data > current.data:
            parent = current
            current = current.right
        else:
            pass  # Element is in the tree pointed at by current
    if current is None:
        return False  # Element is not in the tree

    # Case 1: current has no left child
    if current.left is None:
        # Connect the parent with the right child of the current node
        # Special case, assume the node being deleted is at root
        if parent is None:
            current = current.right
        else:
            # Identify if parent left or parent right should be connected
            if data < parent.data:
                parent.left = current.right
            else:
                parent.right = current.right
    else:
        # Case 2: The current node has a left child
        # Locate the rightmost node in the left subtree of
        # the current node and also its parent
        parent_of_right_most = current
        right_most = current.left
        while right_most.right is not None:
            parent_of_right_most = right_most
            right_most = right_most.right  # Keep going to the right

        # Replace the element in current by the element in rightMost
        current.element = right_most.element
        # Eliminate rightmost node
        if parent_of_right_most.right == right_most:
            parent_of_right_most.right = right_most.left
        else:
            # Special case: parent_of_right_most == current
            parent_of_right_most.left = right_most.left
    return True  # Element deleted successfully


def bst_del_rec(root, data):
    """
    Delete data in BST rooted at root and return the tree;

    Assume root is the root of a Binary Search Tree.

    :param root: root of a binary search tree.
    :type root: BinaryTree
    :param data: data to delete from BST, if exists.
    :type data: object

    >>> b = BinaryTree(5)
    >>> b1 = bst_insert(b, 3)
    >>> b2 = bst_insert(b1, 8)
    >>> b1 = bst_del_rec(b1, 3)
    >>> print(b1)
        8
    5
    <BLANKLINE>
    >>> b4 = BinaryTree(5)
    >>> b4 = bst_insert(b4, 3)
    >>> b4 = bst_insert(b4, 8)
    >>> b4 = bst_del_rec(b4, 5)
    >>> print(b4)
        8
    3
    <BLNKlINE>
    """
    if root is None:
        return None
    elif data < root.data:
        root.left = bst_del_rec(root.left, data)
    elif data > root.data:
        root.right = bst_del_rec(root.right, data)
    elif not root.left:
        root = root.right
    else:
        largest_node = largest(root.left)
        root.data = largest_node.data
        root.left = bst_del_rec(root.left, largest_node.data)
    return root


def largest(r):
    """
    Return the node that contains the largest data in BST r
    :param r: a binary search tree
    :type r: BinaryTree
    :rtype: BinaryTree
    """
    if not r.right:
        return r
    else:
        return largest(r.right)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
