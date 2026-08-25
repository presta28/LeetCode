# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def delete(node, key):
            if node == None:
                return None

            if key < node.val:
                node.left = delete(node.left, key)

            elif key > node.val:
                node.right = delete(node.right, key)

            else:
                # 0 children
                if node.left == None and node.right == None:
                    return None

                # only right child
                if node.left == None:
                    return node.right

                # only left child
                if node.right == None:
                    return node.left

                # 2 children
                successor = node.right

                while successor.left != None:
                    successor = successor.left

                node.val = successor.val

                # delete successor from right subtree
                node.right = delete(node.right, successor.val)

            return node

        return delete(root, key)