import copy 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        for i in range(len(s2)):
            if s2[i] not in s1:
                left = i+1
            elif (s2[i] in s1) and s2[left:i+1].count(s2[i]) > s1.count(s2[i]):
                while (s2[i] in s1) and s2[left:i+1].count(s2[i]) > s1.count(s2[i]):
                    left += 1
            else:
                if i-left+1 == len(s1):
                    return True
        return False