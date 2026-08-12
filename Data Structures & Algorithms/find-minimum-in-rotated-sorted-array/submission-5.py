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
        mid = (l+r)//2
        something about checking the ends also 
        get the middle element
        if the one after it is smaller than what 
            l = mid + 1
        if the one before it is smaller
            r = mid - 1
        correct value is when number before and after it is bigger
        '''
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:   # drop is to the right → min is right of mid
                l = mid + 1
            else:                     # mid could be the min, or it's left of mid
                r = mid
        return nums[l]