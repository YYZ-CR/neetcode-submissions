class Solution:
    def isPalindrome(self, s: str) -> bool:
        back = len(s)
        for i in range(len(s)):
            if not (s[i].isalpha() or s[i].isdigit()):
                continue
            back -= 1
            while not (s[back].isalpha() or s[back].isdigit()):
                back -= 1
            if s[i].lower() != s[back].lower():
                return False
            if i > back:
                return True
        return True
