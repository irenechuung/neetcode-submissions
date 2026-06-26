class Solution:

    def encode(self, strs: List[str]) -> str:
        en=""
        for i in range(0,len(strs)):
            en+=strs[i]
            if i!=len(strs)-1:
                en+="_"
        return en

    def decode(self, s: str) -> List[str]:
        return s.split("_")     