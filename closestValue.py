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

root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(24)
root.right.right.left = TreeNode(22)

result = closestValue(root, 3)
print(result)
