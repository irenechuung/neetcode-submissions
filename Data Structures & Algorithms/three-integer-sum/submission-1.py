class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # intuition: sort it –> left side would be small –> right side would be big
        # have another pointer in the middle?
        # make a set so there's no duplicates?
        # try da sum if its > 0 hmm u can move left pointer down or right poitner down
        #            if < 0 thne u move left pointer right /+ right poitner right
        #            if = 0 add triple tot he set 
        # brute force is to check every triplet –> better? 
        # check every duo and then check if that sum is in hte array (but that lookup mihgt be o(n) too)
        # nums[i]+nums[j]+nums[k]==0
        # nums[i]=-(nums[j]+nums[k])
        # think about how to efficiently find j and k
        # for every index i: run two pointer on indices to the right of i
        # leftmost=l=i+1, rightmost=r=len(nums)-1
        # intended amount = nums[i]
        # if nums[l]+nums[r]==-(nums[i])=> pair! 
        # if < intended => want to make it bigger => increment left 
        # if > intended => increment right 
        # if = intended => add to list
        # keep going as long as left < right
        output=[]
        nums.sort()
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            target = nums[i]*-1
            while(j<k):
                sum=(nums[j]+nums[k])
                if(sum==target):
                    output.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif(sum<target):
                    j+=1
                else:
                    k-=1
        return output
