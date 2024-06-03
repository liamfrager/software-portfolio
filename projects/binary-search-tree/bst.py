class BSTNode():
    def __init__(self, value=None) -> None:
        # VALUE
        self.value = value
        # RELATIONSHIPS
        self.left: BSTNode = None
        self.right: BSTNode = None
        # WEIGHTS
        self.balance = 0

    def insert(self, val) -> None:
        '''Inserts a node into the BST.'''
        if not self.value:
            self.value = val
        elif val >= self.value:
            self.balance += 1
            if self.right:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)
        elif val < self.value:
            self.balance -= 1
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)
        else:
            raise Exception

        # TODO: Rebalance tree after insertion.
        if self.balance > 1:
            if val < self.right.value:
                self.right._rotate_right()
            self._rotate_left()
        if self.balance < -1:
            if val > self.left.value:
                self.left._rotate_left()
            self._rotate_right()

    def find(self, value) -> bool:
        '''Returns TRUE if value is in the tree'''
        if self.value == value:
            return True
        elif value < self.value and self.left:
            return self.left.find(value)
        elif value >= self.value and self.right:
            return self.right.find(value)
        else:
            return False

    def delete(self, value) -> None:
        '''Removes a node from the BST.'''
        if self.value == value:
            if self.left == None:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            elif self.right == None:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
            else:
                # Place the right subtree of the deleted node at largest end of left subtree of the deleted node
                largest_on_left = self.left
                while largest_on_left.right:
                    largest_on_left = largest_on_left.right
                largest_on_left.right = self.right
                # Reassign values
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left

        elif value >= self.value and self.right:
            self.right.delete(value)
        elif value < self.value and self.left:
            self.left.delete(value)
        else:
            raise Exception

        # TODO: rebalance after delete

    def _rotate_right(self) -> None:
        x = self
        x.left = self.left.right
        self = self.left
        self.right = x
        self.balance += 2  # TODO: recalculate weights after rotation.

    def _rotate_left_right(self) -> None:
        pass

    def _rotate_left(self) -> None:
        x = self
        x.right = self.right.left
        self = self.right
        self.left = x
        self.balance -= 2  # TODO: recalculate weights after rotation.

    def _rotate_right_left(self) -> None:
        pass

    @property
    def values(self) -> list[int]:
        '''Prints all values of the BST in order.'''
        vals = []

        def iterate(node: BSTNode):
            if node.left:
                iterate(node.left)
            if node.value:
                vals.append(node.value)
            if node.right:
                iterate(node.right)

        iterate(self)
        return vals

    @property
    def weights(self) -> list[int]:
        '''Prints all values of the BST in order.'''
        weights = []

        def iterate(node: BSTNode):
            if node.left:
                iterate(node.left)
        # if node.weight:
            weights.append(node.balance)
            if node.right:
                iterate(node.right)

        iterate(self)
        return weights

    @property
    def min(self) -> int:
        node = self
        while node.left:
            node = node.left
        return node.value

    @property
    def max(self) -> int:
        node = self
        while node.right:
            node = node.right
        return node.value
