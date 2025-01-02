"""
백준 5639 이진 검색 트리 (골드4)

1. 이진탐색트리 일부 구현
2. 전위순회 결과 트리에 주입
3. 후위순회 진행
"""

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            parent = self.root
            child = self.root
            while child is not None:
                if key < parent.key:
                    parent, child = child, parent.left
                else:
                    parent, child = child, parent.right
            if key < parent.key:
                parent.left = Node(key)
            else:
                parent.right = Node(key)

    def postorder_traversal(self):
        def print_key(node):
            if node.left is not None:
                print_key(node.left)
            if node.right is not None:
                print_key(node.right)
            print(node.key)
        print_key(self.root)


from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
tree = BinarySearchTree()
for i in stdin:
    tree.add(int(i))
tree.postorder_traversal()






