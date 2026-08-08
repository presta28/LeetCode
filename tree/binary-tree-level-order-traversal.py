# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        front = 0
        answer = []
        while front < len(queue):
            level = []
            level_size = len(queue) - front
            count = 0
            while count < level_size:
                node = queue[front]
                front = front + 1
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                count = count + 1
            answer.append(level)
        return answer