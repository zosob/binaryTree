# Write a Python program to check whether a given a binary tree is a valid binary search tree (BST) or not

##Creating tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Check for BST 
def isBST(root):
    stack = []
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.val <= prev:
            return False
        prev = root
        root = root.right
    return True
