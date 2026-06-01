class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        t_list = [0]*58
        s_list = [0]*58
        for i in t:
            t_list[ord(i)-65] += 1

        left = 0
        correct = 0
        required = sum(1 for x in t_list if x > 0)
        shortest = float('inf')
        shortest_str = ""
        for i in range(len(s)):
            s_list[ord(s[i])-65] += 1
            if s_list[ord(s[i])-65] == t_list[ord(s[i])-65]:
                correct += 1
            if correct >= required:
                while correct >= required:
                    if i-left+1 < shortest:
                        shortest = i-left+1
                        shortest_str = s[left:i+1]
                    s_list[ord(s[left])-65] -= 1
                    if s_list[ord(s[left])-65] < t_list[ord(s[left])-65]:
                        correct -= 1
                    left += 1

        return shortest_str