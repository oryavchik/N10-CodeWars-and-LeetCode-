"""Delete Node in a BST"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """Solution"""
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """Function deletes node"""
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        if key == root.val:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            el = root.right
            while el.left:
                el = el.left

            root.val = el.val
            root.right = self.deleteNode(root.right, el.val)
        return root
