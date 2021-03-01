#Deleting a node in BST

#Creating tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deleteNode(root, key):
    #if root doesn't exist
    if not root:
        return root
    # If smaller, then left subtree
    if root.val>key:
        root.left = deleteNode(root.left,key)
    #If greater, then right subtree
    elif root.val<key:
        root.left = deleteNode(root.right, key)
    #if root equal to key
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right

        #Replace minimum value from right tree and remove from right tree

        temp = root.right
        min_val = temp.val
        while temp.left:
            temp = temp.left
            min_val = temp.val
        root.right = deleteNode(root.right, root.val)
    return root
    
def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)
