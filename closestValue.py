#Find the closest value of a target in a given non-empty
#Binary Search Tree (BST) of unique values

#Describing tree
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


#Defining closest value 
def closestValue(root, target):
    a = root.val
    child = root.left if target<a else root.right
    if not child:
        return a
    b = closestValue(child, target)
    return min((a,b), key=lambda x: abs(target-x))
