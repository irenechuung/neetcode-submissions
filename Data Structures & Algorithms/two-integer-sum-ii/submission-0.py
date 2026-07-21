class Solution:
    # Brainstorming:
    # left pointer: index 1, right pointer: last indext (len(numbers)-1)
    # chek if num[ind1]+num[ind2]==target => then return [ind1, ind2]
    # two for loops
    # increase ind1 after ind1==ind2
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(0,len(numbers)-1): 
            for j in range(len(numbers)-1,i,-1): # go backwards 
                if(numbers[i]+numbers[j]==target):
                    return [i+1, j+1]