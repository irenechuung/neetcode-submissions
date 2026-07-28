class Solution:
    def isValid(self, s: str) -> bool:
           
            # go through every character in string for each one
            # check if it's in the stack 
            # add to stack as long as the element isn't in the stack 
            # if it is then pop the stack and check that its = to what was popped
                # if not => return false
            # after all char's are checked => return true 
        
        stack = []
        map = {"}": "{", ")": "(", "]": "["}
        for c in s:
            if(c in map and map[c] in stack):
                popped=stack.pop()
                if popped != map[c]:
                    return False
            else:
                stack.append(c)
        return (stack==[])