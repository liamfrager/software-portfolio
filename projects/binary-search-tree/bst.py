import copy


class BSTNode():
    def __init__(self, value=None) -> None:
        # VALUE
        self.value = value
        # RELATIONSHIPS
        self.left: BSTNode = None
        self.right: BSTNode = None
        # WEIGHTS
        self.height = 0

    def __repr__(self) -> str:
        layers = self.height if self.height < 4 else 3
        bracket_lead_indent = 2
        num_lead_indent = 0
        num_gap = 1
        for _ in range(layers):
            bracket_lead_indent = bracket_lead_indent * 2 + 1
            num_lead_indent = num_lead_indent * 2 + 2
            num_gap = num_gap * 2 + 3

        tree = f'\n{' ' * num_lead_indent}{f'00{self.value}'[-3:]}'
        for layer in range(layers):
            # add bracket layer
            tree += '\n'
            bracket_lead_indent = int((bracket_lead_indent - 1) / 2)
            bracket_width = (2 ** (layers - layer)) - 1
            bracket_gap = num_gap - ((layers - 1 - layer) * 2)
            tree += ' ' * bracket_lead_indent
            for i in range(2 ** layer):
                tree += '/' if self.left else ' '
                tree += ' ' * bracket_width
                tree += '\\' if self.right else ' '
                tree += ' ' * bracket_gap

            # add number layer
            tree += '\n'
            num_gap = int((num_gap - 3) / 2)
            num_lead_indent = int((num_lead_indent - 2) / 2)
            tree += ' ' * num_lead_indent
            for i in range(2 ** layer):
                tree += f'00{self.left.value}'[-3:] if self.left else '   '
                tree += ' ' * num_gap
                tree += f'00{self.right.value}'[-3:] if self.right else '   '
                tree += ' ' * num_gap
        tree += '\n'

        return tree

        def iterate(node: BSTNode) -> str:
            if node.value:
                return node.__repr__()
            if node.left:
                iterate(node.left)
            if node.right:
                iterate(node.right)
        tree = '''
                              014
                           /       \
                      012             013
                     /   \           /   \
                  008     009     010     011
                  / \     / \     / \     / \
                000 001 002 003 004 005 006 007
            '''

    @property
    def balance(self):
        r = 0 if self.right == None else 1 + self.right.height
        l = 0 if self.left == None else 1 + self.left.height
        return r - l

    def recalculate_height(self) -> int:
        if self.left and self.right:
            return 1 + max(self.left.height, self.right.height)
        if self.right:
            return 1 + self.right.height
        if self.left:
            return 1 + self.left.height
        return 0

    def insert(self, val) -> None:
        '''Inserts a node into the BST.'''
        if not self.value:
            self.value = val
        elif val >= self.value:
            if self.right:
                self.right.insert(val)
                self.height = self.right.height + 1  # extend height
            else:
                self.right = BSTNode(val)
                if not self.left:  # extend height
                    self.height += 1
        elif val < self.value:
            if self.left:
                self.left.insert(val)
                self.height = self.right.height + 1  # extend height
            else:
                self.left = BSTNode(val)
                if not self.right:  # extend height
                    self.height += 1
        else:
            raise Exception

        # rebalance tree after insertion.
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
        x = copy.deepcopy(self)
        x.left = copy.deepcopy(self.left.right)
        self = copy.deepcopy(self.left)
        self.right = x
        # recalculate heights
        self.right.height = self.right.recalculate_height()
        self.height = self.recalculate_height()

    def _rotate_left(self) -> None:
        x = copy.deepcopy(self)
        x.right = copy.deepcopy(self.right.left)
        self = copy.deepcopy(self.right)
        self.left = x
        # recalculate heights
        self.left.height = self.left.recalculate_height()
        self.height = self.recalculate_height()

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
