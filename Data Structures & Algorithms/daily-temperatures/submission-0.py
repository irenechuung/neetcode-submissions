class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        problem understanding:
        given an array fo temps 
        want to output an array of same size
        for each position in the array, like u want to count # of days after it until u hit a day with higher temp
        brute force is O(N^2), how to make it O(N)?
        stack
        empty array output 
        something about going through the elements in reverse
        last element is always 0
        resetting when u run into na element that is smaller than the top 
        [40 35 36 ], run into 30
        '''
        output = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                stackT, stackInd = stack.pop()
                output[stackInd]=i-stackInd
            stack.append((t,i))
        return output
