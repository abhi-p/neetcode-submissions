class ListNode:
    def __init__(self, val,next_node=None):
        self.val=val
        self.next=next_node
class LinkedList:
    
    def __init__(self): 
        self.head=ListNode(-1)
        self.tail=self.head

      # -1->1->2->3->4->5
    def get(self, index: int) -> int:
        i=0
        curr=self.head.next
        while curr:
            if i==index:
                return curr.val
            curr=curr.next
            i+=1
        return -1

        

    def insertHead(self, val: int) -> None:
        node=ListNode(val)

        node.next=self.head.next
        self.head.next=node

        if node.next==None:
            self.tail=self.head.next

    def insertTail(self, val: int) -> None:
        node=ListNode(val)

        if self.head.next!=None:
            self.tail.next=node
            self.tail=node
        else:
            self.insertHead(val)
        
        

    def remove(self, index: int) -> bool:
        i=0
        curr=self.head

        while i<index and curr:
            curr=curr.next
            i+=1

        if curr and curr.next:
            if curr.next==self.tail:
              self.tail=curr
            curr.next=curr.next.next
            return True
        return False  
        

    def getValues(self) -> List[int]:
        curr=self.head.next
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        return arr
            
        
