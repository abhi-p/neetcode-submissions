# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def findMin(root):
            while root and root.left:
                root=root.right
            return root.val
        
        def remove(root,key):
            if not root:
                return None
            
            if root.val>key:
                root.left=remove(root.left,key)
            elif root.val<key:
                root.right=remove(root.right,key)
            else:
                if not root.left and not root.right:
                    return None
                elif not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    root.val=findMin(root)
                    root.right=remove(root.right,root.val )
                    


            return root
        return remove(root,key)