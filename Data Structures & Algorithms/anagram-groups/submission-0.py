class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            okay think of one solution first (can be slow)

            okay make a hashmap for each string.:
                character => # of times it's in the word 
            
            go thru every word:
                make a hashmap of that word
                see if it's already been seen 

            okay i thinmk too complicated

            keep hashmap to keep track of stuff 
                since output is the words
                map alphabetical => word 
            try sorting every string alphabetically and combining it back to string
            if sorted string is a key in hashmap => add word to array at map[key]
            otherwise: map[key]=string 

            make empty arrya
            go through every value (array) hashmap 
                append to array 
        '''
        alpha=defaultdict()
        for words in strs:
            rearranged="".join(sorted(words))
            if rearranged in alpha:
                alpha[rearranged].append(words)
            else:
                alpha[rearranged]=[words]
        
        output=[]
        for keys in alpha:
            output.append(alpha[keys])
        return output



