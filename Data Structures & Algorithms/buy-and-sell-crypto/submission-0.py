class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = len(prices)-1
        # only want to move the left one if moving it ups ur profit same thing with right
        # incrementing left is good if it's smaller 
        # incrementing right is good if it's bigger 
        r_max = 0 # start with default value
        l_min = 0
        r_ind=0
        l_ind=0
        while l<r:
            if (l==0 or prices[l]<l_min):
                l_min=prices[l]
                l_ind=l
            if(r==len(prices)-1 or prices[r]>r_max):
                r_max=prices[r]
                r_ind=0
            l+=1
            r-=1
        return max(0,(r_max-l_min))
