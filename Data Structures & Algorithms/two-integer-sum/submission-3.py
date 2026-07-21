class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        brute force:
        time = O(N^2)
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
        '''

        hashmap={}
        for i in range(0,len(nums)):
            n = nums[i]
            diff = target - n
            if(diff in hashmap):
                return [hashmap[diff], i]
            else:
                hashmap.add(diff)