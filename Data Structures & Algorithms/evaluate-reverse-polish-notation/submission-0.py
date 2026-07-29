class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        have an empty stack
        have an output int array 
        as long as it's not an operator (+, -, *, /) push to stack 
            when u hit an operator then u want to execute the operation 
            make sure u reverse it cause stack is last in first out 
                top = first pop
                bottom = second pop 
                
                bottom operator top 
        '''

        stack = []
        output = 0
        for part in tokens:
            if(part not in "+_*/"):
                stack.append(part)
            else:
                piece = 0
                top = stack.pop()
                bottom = stack.pop()
                if(part == "+"):
                    piece = int(bottom) + int(top)
                elif(part == "-"):
                    piece = int(bottom) - int(top)
                elif(part == "*"):
                    piece = int(bottom) * int(top)
                else:
                    piece = int(int(bottom)/int(top))
                stack.append(piece)
        return stack[-1]