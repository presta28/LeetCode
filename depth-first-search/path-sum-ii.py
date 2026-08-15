# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        answer = []
        liist = []

        def path(node, targetSum, current_sum):

            if node == None:
                return

            liist.append(node.val)
            current_sum += node.val

            if node.left == None and node.right == None:
                if current_sum == targetSum:
                    answer.append(liist.copy())

                liist.pop()
                return

            path(node.left, targetSum, current_sum)
            path(node.right, targetSum, current_sum)

            liist.pop()

        path(root, targetSum, 0)
        return answer