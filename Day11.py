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
        return self.maxDepthAndDiameterOfTheNode(root)[0]

    def maxDepthAndDiameterOfTheNode(self, node) -> (int, int):
        leftTouple = (0, 0)
        rightTouple = (0, 0)
        if node.left != None:
            leftTouple = self.maxDepthAndDiameterOfTheNode(node.left)
            leftTouple = (leftTouple[0], leftTouple[1] + 1)
        if node.right != None:
            rightTouple = self.maxDepthAndDiameterOfTheNode(node.right)
            rightTouple = (rightTouple[0], rightTouple[1] + 1)
        maxDiaAtCurrentNode = abs(leftTouple[1] + rightTouple[1])
        maxDiaSoFor = max(maxDiaAtCurrentNode, leftTouple[0], rightTouple[0])
        maxDepthAtCurrentNode = max(leftTouple[1], rightTouple[1])
        return (maxDiaSoFor, maxDepthAtCurrentNode)


def testTheSolution():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    return root


print(Solution().diameterOfBinaryTree(testTheSolution()))


