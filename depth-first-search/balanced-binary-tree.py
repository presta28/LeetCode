# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):

            if node is None:
                return 0

            left_height = height(node.left)

            if left_height == -1:
                return -1

            right_height = height(node.right)

            if right_height == -1:
                return -1

            difference = left_height - right_height

            if difference > 1 or difference < -1:
                return -1

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

        if height(root) == -1:
            return False

        return True