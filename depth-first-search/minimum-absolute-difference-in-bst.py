# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        minimum = float("inf")
        previous = None

        def getmin(node):
            nonlocal minimum, previous

            if node == None:
                return

            # Left subtree
            getmin(node.left)

            # Current node
            if previous != None:
                diff = node.val - previous

                if diff < minimum:
                    minimum = diff

            # Current node ab previous ban jayega
            previous = node.val

            # Right subtree
            getmin(node.right)

        getmin(root)

        return minimum

        