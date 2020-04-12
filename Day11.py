'''
Diameter of binary tree: Longest path between any two nodes of a tree
So the idea is for every node calculate max depth and langest path 
Then recurse and keep doing it for every node and keep updating local maxima
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxDia = 0

        def maxDepth(node) -> int:
            left, right = 0, 0
            if node.left != None:
                left = maxDepth(node.left) + 1
            if node.right != None:
                right = maxDepth(node.right) + 1

            self.maxDia = max(self.maxDia, (left + right))
            return max(left, right)

        if root == None:
            return 0
        else:
            maxDepth(root)
            return self.maxDia


def testTheSolution():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    return root


print(Solution().diameterOfBinaryTree(TreeNode(1)))
