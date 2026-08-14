# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def pathsum(node, current_sum):

            if node == None:
                return False

            current_sum += node.val

            # leaf node
            if node.left == None and node.right == None:
                return current_sum == targetSum

            left_ans = pathsum(node.left, current_sum)

            if left_ans:
                return True

            right_ans = pathsum(node.right, current_sum)

            if right_ans:
                return True

            return False

        return pathsum(root, 0)

        