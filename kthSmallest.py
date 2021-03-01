#kthSmallest Value in BST
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def kthSmallest(root, key):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k-=1
        if k == 0:
            break
        root = root.right
    return root.val
