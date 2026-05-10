class TreeNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.left=None
        self.right=None
class TreeMap:
    
    def __init__(self):
        self.root=None


    def insert(self, key: int, val: int) -> None:
        node=TreeNode(key,val)
        if not self.root:
            self.root=node

        curr=self.root
        while True:
            if key<curr.key:
                if curr.left==None:
                    curr.left=node
                    return
                else:
                    curr=curr.left

            elif key>curr.key:
                if not curr.right:
                    curr.right=node
                    return
                curr=curr.right
                
            else:
                curr.val=val
                return


    def get(self, key: int) -> int:
        curr=self.root

        while curr:
            if curr.key==key:
                return curr.val
            elif key<curr.key:
                curr=curr.left
            else:
                curr=curr.right
        return -1


    def getMin(self) -> int:
        if not self.root:
            return -1
        curr=self.root
        while curr and curr.left:
            curr=curr.left
        return curr.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        curr=self.root
        while curr and curr.right:
            curr=curr.right
        return curr.val


    def remove(self, key: int) -> None:
        self.root=self.removeH(self.root,key)
        print("in Remove")

    def removeH(self,curr,key):
         if not curr:
             return None
         if key>curr.key:
             curr.right=self.removeH(curr.right,key)
         elif key<curr.key:
             curr.left=self.removeH(curr.left,key)
         else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                minNode=self.getMinNode(curr.right)
                curr.key=minNode.key
                curr.val=minNode.val
                curr.right=self.removeH(curr.right,minNode.key)
            return curr

    def getMinNode(self,node):
        curr=node
        while curr and curr.left:
            curr=curr.left
        return curr
            



    def getInorderKeys(self) -> List[int]:
        if self.root==None:
            return []
        res=[]
        self.inOrder(self.root,res)
        return res

    def inOrder(self,curr,res):
        if not curr:
            return
        self.inOrder(curr.left,res)
        res.append(curr.key)
        self.inOrder(curr.right,res)



