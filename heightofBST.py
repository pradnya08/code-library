# get the height of a Binary Search Tree.

def height(root):
    if root is not None:
        return max(1 + height(root.left), 1 + height(root.right))
    else:
        return -1
    