class Solution:

    def encode(self, strs: List[str]) -> str:
        en=""
        for i in range(0,len(strs)):
            en+=strs[i]
            if i!=len(strs)-1:
                en+="_"
        return en

    def decode(self, s: str) -> List[str]:
        list=s.split("_")     
        if(len(list)==1):
            return []
        return list