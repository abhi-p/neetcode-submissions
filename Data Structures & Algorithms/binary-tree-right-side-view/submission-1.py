# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        que=deque()
        if not root:
            return []
        ret=[]

        que.append(root)

        while que:
            for i in range(len(que)):
                node=que.popleft()

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            ret.append(node.val)

        return ret
        