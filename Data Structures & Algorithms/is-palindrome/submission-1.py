class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(0,(int)(len(s)/2)):
            if(i>(len(s)-i-1)):
                return True
            
            if(s[i]!=s[len(s)-i-1]):
                return False
        return True