class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
        thought process
            don't think should check adjacent elemernts 
            instead:
                can compare against left and rihg pointer 
                if (curr > nums[l] and curr > target) and :
                    check right side 
                if curr > nums[l] and curr < target:
                    check left side 
                if curr < nums[r] and nums[r]<target:
                    check left side 
                if curr < nums[r] and nums[r]>target:
                    check right side 

                    
        '''
        l = 0
        r = len(nums)-1
    
        while l<=r:
            mid = (l+r)//2
            curr = nums[mid]
            x = (curr > nums[l] and curr > target) or (curr < nums[r] and nums[r]>target)
            y = (curr > nums[l] and curr < target) or (curr < nums[r] and nums[r]<target)
            if curr == target:
                return mid
            if x:
                l = mid+1
            else:
                r=mid-1
            
        return -1