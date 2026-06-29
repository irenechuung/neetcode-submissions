class Solution:

    def encode(self, strs: List[str]) -> str:
        en=""
        for i in range(0,len(strs)):
            if strs[i]!="_":
                en+=strs[i]
            elif strs[i]=="":
                en+="meow"
            else:
                en+="&"
            if i!=len(strs)-1:
                en+="_"
        return en

    def decode(self, s: str) -> List[str]:
        list=s.split("_")     
        for i in range(0,len(list)):
            if(list[i]=="meow"):
                list[i]==""
            elif(list[i]=="&"):
                list[i]=_
        if(list==[""]):
            return []
        return list