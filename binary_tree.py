class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def detailed(root):
    if root is None:
        return
    else:
        print(root.data, ":", end="")
        if root.left is not None:
            print("L", root.left.data, end=",")

        if root.right is not None:
            print("R", root.right.data)

        print()

        detailed(root.left)
        detailed(root.right)


def insert():
    data = int(input())

    if data == -1:
        return
    root = Tree(data)
    root.left = insert()
    root.right = insert()

    return root
def deleteleaves(root):
    if root==None:
        return None
    if root.left==None and root.right==None:
        return None
    root.left=deleteleaves(root.left)
    root.right=deleteleaves(root.right)
    #del root

    return root


root = insert()
detailed(root)
deleteleaves(root)
detailed(root)
