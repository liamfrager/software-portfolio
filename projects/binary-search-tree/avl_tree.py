import copy


class AVLNode():
    def __init__(self, value: 'None | int | AVLNode' = None) -> None:
        # VALUE
        self.value = value.value if type(value) == AVLNode else value
        # RELATIONSHIPS
        self.left: AVLNode = value.left if type(value) == AVLNode else None
        self.right: AVLNode = value.right if type(value) == AVLNode else None
        # WEIGHTS
        self.height = value.height if type(value) == AVLNode else 0

    def __repr__(self) -> str:
        if not self:
            return 'This AVL Tree has no values.'
        else:
            # establish gaps based on number of layers in tree
            layers = self.height if self.height < 4 else 3
            bracket_lead_indent = 2
            num_lead_indent = 0
            num_gap = 1
            for _ in range(layers):
                bracket_lead_indent = bracket_lead_indent * 2 + 1
                num_lead_indent = num_lead_indent * 2 + 2
                num_gap = num_gap * 2 + 3

            # start tree with root value
            tree = f'\n{' ' * num_lead_indent}{f'00{self.value}'[-3:]}'
            nodes = [self]
            for layer in range(layers):
                # add bracket layer
                tree += '\n'
                bracket_lead_indent = int((bracket_lead_indent - 1) / 2)
                tree += ' ' * bracket_lead_indent
                bracket_width = (2 ** (layers - layer)) - 1
                bracket_gap = num_gap - ((layers - 1 - layer) * 2)
                for node in nodes:
                    if node:
                        tree += '/' if node.left else ' '
                        tree += ' ' * bracket_width
                        tree += '\\' if node.right else ' '
                        tree += ' ' * bracket_gap
                    else:
                        tree += ' ' * (bracket_width + bracket_gap + 2)

                # add number layer
                tree += '\n'
                num_lead_indent = int((num_lead_indent - 2) / 2)
                tree += ' ' * num_lead_indent
                num_gap = int((num_gap - 3) / 2)
                for node in nodes:
                    if node:
                        tree += f'00{node.left.value}'[-3:] \
                            if node.left else '   '
                        tree += ' ' * num_gap
                        tree += f'00{node.right.value}'[-3:] \
                            if node.right else '   '
                        tree += ' ' * num_gap
                    else:
                        tree += ' ' * ((num_gap + 3) * 2)

                # get nodes of next layer
                new_nodes = []
                for node in nodes:
                    if node:
                        new_nodes.append(node.left)
                        new_nodes.append(node.right)
                    else:
                        new_nodes.append(None)
                        new_nodes.append(None)
                nodes = new_nodes

            if self.height > 3:
                tree += '\n'
                for node in nodes:
                    if node:
                        tree += '/ ' if node.left else '  '
                        tree += '\ ' if node.right else '  '
                    else:
                        tree += '    '

            tree += '\n'

            return tree
        #                   014
        #                /       \
        #           012             013
        #          /   \           /   \
        #       008     009     010     011
        #       / \     / \     / \     / \
        #     000 001 002 003 004 005 006 007
        #     / \ / \ / \ / \ / \ / \ / \ / \

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

    def insert(self, value: 'int | AVLNode'):
        '''Inserts an ancestor node with a given value.'''
        if type(value) == AVLNode:
            val = value.value
        else:
            val = value

        if not self.value:
            self.value = val
        elif val >= self.value:
            if self.right:
                self.right = self.right.insert(value)
                self.height = self.recalculate_height()  # extend height
            else:
                self.right = AVLNode(value)
                if not self.left:  # extend height
                    self.height += 1
        elif val < self.value:
            if self.left:
                self.left = self.left.insert(value)
                self.height = self.recalculate_height()  # extend height
            else:
                self.left = AVLNode(value)
                if not self.right:  # extend height
                    self.height += 1
        else:
            raise Exception

        # rebalance tree after insertion.
        if self.balance > 1:
            if val < self.right.value:
                self.right = self.right._rotate_right()
            self = self._rotate_left()
        if self.balance < -1:
            if val > self.left.value:
                self.left = self.left._rotate_left()
            self = self._rotate_right()
        return self

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
        '''Removes an ancester node with a given value.'''
        if self.value == value:
            if not self.left and self.right:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            elif not self.right and self.left:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
            elif self.left and self.right:
                # Insert right node after the right node.
                self = self.left.insert(self.right)
            else:
                # does not need to rebalance when deleting leaf node.
                return None
        elif value >= self.value and self.right:
            self.right.delete(value)
        elif value < self.value and self.left:
            self.left.delete(value)
        else:
            raise Exception

        # TODO: rebalance after delete
        # rebalance tree after deletion.
        if self.balance > 1:
            if value < self.right.value:
                self.right = self.right._rotate_right()
            self = self._rotate_left()
        if self.balance < -1:
            if value > self.left.value:
                self.left = self.left._rotate_left()
            self = self._rotate_right()
        return self

    def _rotate_right(self) -> None:
        x = copy.deepcopy(self)
        x.left = copy.deepcopy(self.left.right)
        self = copy.deepcopy(self.left)
        self.right = x
        # recalculate heights
        self.right.height = self.right.recalculate_height()
        self.height = self.recalculate_height()
        return self

    def _rotate_left(self) -> None:
        x = copy.deepcopy(self)
        x.right = copy.deepcopy(self.right.left)
        self = copy.deepcopy(self.right)
        self.left = x
        # recalculate heights
        self.left.height = self.left.recalculate_height()
        self.height = self.recalculate_height()
        return self


class AVLTree():
    def __init__(self):
        self.root: AVLNode | None = None

    def __repr__(self):
        return self.root.__repr__()

    def insert(self, value):
        '''Inserts a node with the given value into the AVL tree.'''
        if self.root == None:
            self.root = AVLNode(value)
        else:
            self.root = self.root.insert(value)

    def delete(self, value):
        '''Deletes a node with the given value from the AVL tree.'''
        if self.root == None:
            self.root = AVLNode(value)
        else:
            self.root = self.root.delete(value)

    @property
    def values(self) -> list[int]:
        '''Prints all values of the BST in order.'''
        vals = []

        def iterate(node: AVLNode):
            if node.left:
                iterate(node.left)
            if node.value:
                vals.append(node.value)
            if node.right:
                iterate(node.right)

        iterate(self.root)
        return vals

    @property
    def min(self) -> int:
        if not self.root:
            return None
        else:
            node = self.root
            while node.left:
                node = node.left
            return node.value

    @property
    def max(self) -> int:
        if not self.root:
            return None
        else:
            node = self.root
            while node.right:
                node = node.right
            return node.value
