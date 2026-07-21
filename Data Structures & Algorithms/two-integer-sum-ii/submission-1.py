class Solution:
    # Brainstorming:
    # left pointer: index 1, right pointer: last indext (len(numbers)-1)
    # chek if num[ind1]+num[ind2]==target => then return [ind1, ind2]
    # two for loops
    # increase ind1 after ind1==ind2
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # brute force
        # for i in range(0,len(numbers)-1): 
        #     for j in range(len(numbers)-1,i,-1): # go backwards 
        #         if(numbers[i]+numbers[j]==target):
        #             return [i+1, j+1]

        # Two pointer
        ind1, ind2 = 0, len(numbers)-1 
        while ind1<ind2:
            sum=numbers[ind1]+numbers[ind2]
            if sum==target:
                return [ind1+1, ind2+1]
            elif sum<target:
                ind1+=1
            else:
                ind2-=1
            