class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod=""
        for i in range(0,len(s)):
            if s[i].isalnum():
               mod+=s[i]

        half = (int)(len(mod)/2)
        for i in range(0,half):
            if(mod[i].casefold()!=mod[len(mod)-i-1].casefold()):
                return False
        
        return True