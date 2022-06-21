from Node import Node


class AVLTree:
    def __init__(self, value: Node = None):
        if value is None:
            self.__root = None

        else:
            self.__root = self.insert(value)

    def isEmpty(self) -> bool:
        return self.__root is None

    def insert(self, key):
        if self.__root is None:
            self.__root = Node(key)

        else:
            self.__root = self.__insert(self.__root, key)

    def __insert(self, root, key):
        if not root:
            return Node(key)

        elif key < root.get_value():
            root.set_left(self.__insert(root.get_left(), key))

        else:
            root.set_right(self.__insert(self.__root.get_right(), key))

        root.set_height(1 + max(self.get_height(root.get_left()), self.get_height(root.get_right())))

        balance = self.get_balance(root)

        if balance > 1 and key < root.get_left().get_value():
            return self.__right_rotate(root)

        if balance < -1 and key > root.get_right().get_value():
            return self.__left_rotate(root)

        if balance > 1 and key > root.get_left().get_value():
            root.set_left(self.__left_rotate(root.get_left()))
            return self.__right_rotate(root)

        if balance > -1 and key < root.get_right().get_value():
            root.set_right(self.__right_rotate(root.get_right()))
            return self.__left_rotate(root)

        return root

    def __left_rotate(self, p: Node) -> Node:
        u = p.get_right()
        t2 = u.get_left()
        u.set_left(p)
        p.set_right(t2)
        p.set_height(1 + max(self.get_height(p.get_left()), self.get_height(p.get_right())))
        u.set_height(1 + max(self.get_height(u.get_left()), self.get_height(u.get_right())))
        return u

    def __right_rotate(self, p: Node) -> Node:
        u = p.get_left()
        t2 = u.get_right()
        u.set_right(p)
        p.set_left(t2)
        p.set_height(1 + max(self.get_height(p.get_left()), self.get_height(p.get_right())))
        u.set_height(1 + max(self.get_height(u.get_left()), self.get_height(u.get_right())))
        return u

    def get_height(self, node: Node) -> int:
        if node is None:
            return 0

        return node.get_height()

    def get_balance(self, node: Node) -> int:
        if not node:
            return 0

        return self.get_height(node.get_left()) - self.get_height(node.get_right())

    def __preOrder(self, root: Node):
        if not root:
            return

        print(root.get_value(), end="")
        self.__preOrder(root.get_left())
        self.__preOrder(root.get_right())

    def delete(self, key):
        if self.__root is not None:
            self.__root = self.__delete(self.__root, key)


    def __delete__(self, root: Node, key) -> Node:
        if not root:
            return root

        elif key < root.get_value():
            root.set_left(self.__delete__(root.get_left(), key))

        elif key > root.get_value():
            root.set_right(self.__delete__(root.get_right(), key))

        else:
            if root.get_left() is None:
                temp = root.get_right()
                root = None
                return temp

            elif root.get_right() is None:
                temp = root.get_left()
                root = None
                return temp

            temp = self.get_min_value_node(root.get_right())
            root.set_value(temp.get_value())
            root.set_right(self.__delete(root.get_right(), temp.get_value()))

        if root is None:
            return root

        root.set_height(1 + max(self.get_height(root.get_left()), self.get_height(root.get_right())))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.get_left()) >= 0:
            return self.__right_rotate(root)

        if balance < -1 and self.get_balance(root.get_right()) <= 0:
            return self.__left_rotate(root)

        if balance > 1 and self.get_balance(root.get_left()) < 0:
            root.set_left(self.__left_rotate(root.get_left()))
            return self.__right_rotate(root)

        if balance < -1 and self.get_balance(root.get_right()) > 0:
            root.set_right(self.__right_rotate(root.get_right()))
            return self.__left_rotate(root)


        return root


    def get_root(self) -> Node:
        return self.__root

    def get_min_value_node(self, root: Node) -> Node:
        if root is None or root.get_left() is None:
            return root

        return self.get_min_value_node(root.get_left())
















