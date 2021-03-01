##Creating tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#Making sorted array to BST
def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums)//2
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid+1:])
    return node

#Sorting to preorder tree

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)


result = sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9])
preOrder(result)
