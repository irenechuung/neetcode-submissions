class MinStack:
    stack=[]
    minStack=[]
    def __init__(self):
        self.stack=[]
        self.minStack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if(self.minStack==[]):
            self.minStack.append(val)
        elif(val<self.minStack[-1]):
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
       '''
       brute force is O(N) = searching thru all the elments
            having a list 
            keep track of min when u pop elements into a list
            repush everything back into the stack 
        
        alternative: 
            popping is O(1) in a stack
            if u have another stack that keeps the min elemnt on top 
            then getMIn would be O(1)
       '''
       return self.minStack[-1]
       
