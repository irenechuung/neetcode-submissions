class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        piles = array of ints 
        hr = # of total hours to eat banans 
        b/hr = k 
        can eat k bananas in the hour 
        each hour => can only from one pile 
        
        brute force:
        output = minimum # of k bananas/hr 
        for each pile: 
            amount = piles[i]
            if amount >= k => hours = amount/k
            if amount < k => hours = 1
            sum up hours and check if total hours < h
        n^2 

        how to optimize??
        it's not optimal to have != k bananas because u will have leftovers?
        for the value k, try only values in piles
            => ugh was close, but should try from 1 to max(piles)
        '''
        def check(curr_k, piles):
            total=0
            for element in piles:
                total+=math.ceil(element / curr_k) 
            return total
        # binary search from 1 to max(piles)
        l = 1
        r = max(piles)
        while l<r:
            curr = (l+r)//2
            tot = check(curr, piles)
            if tot <= h:
                r=curr
            else:
                l=curr+1
        return l
            