class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        n cars => position and speed array both are n size
        given a target which is the end destination (car is at end if position ==    
        target)
        
        if car catches up to another => will drive @ same position + speed until the end = car fleet (single car = car fleet)

        at destination = at position == target => how many car fleets will pass by  there

        first thought is that the target is a distance so for each car, u need to be able to continually update its position

        another thought is focusing on in what condition a car catches up to another
        that is when position r the same 

        one way: to increment time continually and keep track of the position at each hour => then car is at same position if their og position + speed * hours r the same 

        other ideas:
        example two positions aren't sorted => should sort positions in ascending order 
        

        after looking at hints: 
        u r given position and speed and a final target position
        
        want to travel some distance (target - og position) given this speed 
        time needed = (target - position)/speed 
        
        calculate the time needed for each car with the formula above 
        
        sort array in descending order (from bigger => smaller)
        - car at farthest right position (biggest og position) has no fleet to catch up to
        push it 
        for each car, check if time <= that car (then it'll be part of that fleet)
        if time > car then push it to stack 
        return size of stqack
        
        want to go in descending order 
        '''
        
        fleets = []
        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        for p, s in pair: 
            fleets.append((target-p)/s)
            if(len(fleets)>=2 and fleets[-1]<=fleets[-2]):
                fleets.pop()
        return len(fleets)

        