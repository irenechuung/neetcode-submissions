class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            brute force => add all characters of one str into array
            go through other word character by character 
                => remove character from array every time 
            

            quicker? 
            hashmap where u go through one string map char => quantity 
            do same for other string
            check if they're the same 

        '''
        sDict=dict()
        tDict=dict()
        for c in s:
            if(c in sDict):
                sDict[c]=sDict[c]+1
            else:
                sDict[c]=1
        for c in t:
            if(c in tDict):
                tDict[c]=tDict[c]+1
            else:
                tDict[c]=1
        return sDict == tDict
        

