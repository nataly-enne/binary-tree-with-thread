from threading import Thread


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                # insert(root.right, node)
                thread_right = Thread(target=insert, args=(root.right, node))
                thread_right.start()
        else:
            if root.left is None:
                root.left = node
            else:
                # insert(root.left, node)
                thread_left = Thread(target=insert, args=(root.left, node))
                thread_left.start()


def search(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)
