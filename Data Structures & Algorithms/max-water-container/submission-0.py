class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Problem understanding:
        # bars represent the boundaries of the contianer
        # smaller bar = heihg tof ocntianer 
        # doesn't matter what quantities within the cotnainer are, just care about width and height of contianer
        # l, r as left and right indicies of boundaries
        # height = smaller of the two heihgts at those values
        # amount of water = height[smaller]*(r-l)
        # start at l = leftmost, r = rightmost
        # only move pointer with smaller pointer (thats the only onet hat matters)
        # move pointer if the (l-r)*height is bigger

        l,r=0,len(heights)-1
        max=0
        while(l<r):
            width=r-l
            min=0
            if(heights[l]<heights[r]):
                min=l
            else:
                min=r
            area=heights[min]*(width)
            if(area>max):
                max=area
            if(min==l):
                l+=1
            else:
                r-=1
        return max