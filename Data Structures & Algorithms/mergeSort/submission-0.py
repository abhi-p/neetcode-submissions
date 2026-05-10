# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs,0,len(pairs)-1)
    
    def mergeSortHelper(self,pairs,start,end):
        if end-start+1<=1:
            return pairs

        mid=(end+start)//2

        self.mergeSortHelper(pairs,start,mid)

        self.mergeSortHelper(pairs,mid+1,end)

        self.merge(pairs,start,mid,end)

        return pairs

    
    def merge(self,arr,start,mid,end):
        l=start
        print("new merger")
        print(start,mid,end)

        while l<end:
            print(arr[l].key)
            l+=1
        L=arr[start:mid+1]
        R=arr[mid+1:end+1]

        i=0
        j=0
        k=start
        while i<len(L) and j<len(R):
            if L[i].key<=R[j].key:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
        print("res")
        for o in range(len(arr)):
            print(arr[o].key)
        

