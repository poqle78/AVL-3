import sys


sys.setrecursionlimit(200000)
q = int(input())
root = None

class Node:
    __slots__ = ('key', 'left', 'right', 'height')

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if node:
        return node.height
    else:
        return 0


def update_height(node):
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    if node:
        return get_height(node.right) - get_height(node.left)
    else:
        return 0

def rotate_left(a):
    b = a.right
    temp = b.left
    b.left = a
    a.right = temp
    update_height(a)
    update_height(b)
    return b

def rotate_right(a):
    b = a.left
    temp = b.right
    b.right = a
    a.left = temp
    update_height(a)
    update_height(b)
    return b

def balance(node):
    update_height(node)
    bal = get_balance(node)

    if bal == 2:
        u = node.right
        if get_balance(u) >= 0:
            return rotate_left(node)
        else:
            node.right = rotate_right(u)
            return rotate_left(node)

    if bal == -2:
        u = node.left
        if get_balance(u) <= 0:
            return rotate_right(node)
        else:
            node.left = rotate_left(u)
            return rotate_right(node)

    return node

def insert(node, key):
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    return balance(node)

def get_min(node):
    curr = node
    while curr and curr.left:
        curr = curr.left
    return curr

def delete(node, key):
    if not node:
        return node
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            temp = get_min(node.right)
            node.key = temp.key
            node.right = delete(node.right, temp.key)

    return balance(node)

def exists(node, key):
    curr = node
    while curr:
        if curr.key == key:
            return True
        elif key < curr.key:
            curr = curr.left
        else:
            curr = curr.right
    return False

def find_next(node, key):
    ans = None
    curr = node
    while curr:
        if curr.key >= key:
            ans = curr.key
            curr = curr.left
        else:
            curr = curr.right
    return ans

def find_prev(node, key):
    ans = None
    curr = node
    while curr:
        if curr.key <= key:
            ans = curr.key
            curr = curr.right
        else:
            curr = curr.left
    return ans

def prnt(node, res):
    if node:
        res.append(str(node.key))
        prnt(node.left, res)
        prnt(node.right, res)

for i in range(q):
    query = input().split()
    cmd = query[0]

    if cmd == 'add':
        x = int(query[1])
        root = insert(root, x)

    elif cmd == 'del':
        x = int(query[1])
        root = delete(root, x)

    elif cmd == 'exists':
        x = int(query[1])
        if exists(root, x):
            print("YES")
        else:
            print("NO")

    elif cmd == 'next':
        x = int(query[1])
        ans = find_next(root, x)
        if ans is None:
            print("None")
        else:
            print(ans)

    elif cmd == 'prev':
        x = int(query[1])
        ans = find_prev(root, x)
        if ans is None:
            print("None")
        else:
            print(ans)


    elif cmd == 'root':
        if root:
            print(root.key)
        else:
            print("Empty")

    elif cmd == 'height':
        print(get_height(root))

    elif cmd == 'print':
        if not root:
            print("Empty")
        else:
            d = []
            prnt(root, d)
            print(" ".join(d))
