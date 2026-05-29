class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range (0,len(strs)):
            for j in range (len(prefix), -1, -1):
                if prefix[0:j+1] == strs[i][0:j+1]:
                    prefix = prefix[0:j+1]
                    break
                if j == 0:
                    return ""
        return prefix