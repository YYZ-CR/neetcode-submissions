class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # so the problem is essentially trying to find when the next max appears 
        # ie finding the local maxes of the data set
        
        t = temperatures
        next_warmer = [0]*len(t)
        stack = [0]
        for i in range(1,len(t)):
            while stack and t[i] > t[stack[-1]]:
                length = i- stack[-1]
                next_warmer[stack.pop()] = length
            stack.append(i)
        return next_warmer