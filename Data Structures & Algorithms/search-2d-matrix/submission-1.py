class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])

        low,high=0,ROWS*COLS-1

        while low<=high:
            mid=low+(high-low)//2
            print(mid,low,high,)
            r,c=mid//COLS, mid%COLS
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                high=mid-1
            else:
                low=mid+1
        return False