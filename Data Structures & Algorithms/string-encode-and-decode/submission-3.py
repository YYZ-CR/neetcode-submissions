class Solution:

    def encode(self, strs: List[str]) -> str:
        s = str()
        for i in range(len(strs)):
            s += str(len(strs[i]))+"#"
            s += strs[i]
        return s
    def decode(self, s: str) -> List[str]:
        strs = list()
        num = ""
        on = True
        for i in s:
            if num == 0:
                    on = True
                    num = ""
            if i == "#" and on:
                on = False
                num = int(num)
                strs.append("")
            elif on:
                num += str(i)
            else: 
                strs[-1] += i
                num -= 1
        return strs
        
