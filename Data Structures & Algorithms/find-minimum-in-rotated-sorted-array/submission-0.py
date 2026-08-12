class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        trying to find the minimum in an array that's been rotated 
        rotated array has two sorted parts: 
            end part (x+1 => max (array))
            front part (1 => x)
        want to find the minimum 
        u want to end up in the part that has the front part
            once u identify that front sorted part of the array
            minimum = most left of that front part 

        l = 0
        r = len(nums)-1
        
        '''
        return min(nums)