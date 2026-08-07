class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        basically its binary search but lik split into an array
        lowkey do same thing just get row and column from the index
        '''

        total = len(matrix)*len(matrix[0])
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = total-1
        while l<=r:
            mid = l + ((r-l)//2)
            currR = (mid // cols) 
            currL = (mid % cols) 
            if matrix[currR][currL]==target:
                return True
            elif matrix[currR][currL]<target:
                l=mid+1
            else:
                r=mid-1
        return False
        