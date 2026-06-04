class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                second = s.pop()
                first = s.pop()
                if i == '+':
                    s.append(int(first)+int(second))
                elif i == '-':
                    s.append(int(first)-int(second))
                elif i == '*':
                    s.append(int(first)*int(second))
                elif i == '/':
                    s.append(int(first)/int(second))
            else: s.append(int(i))
        return int(s[0])
                    
                        