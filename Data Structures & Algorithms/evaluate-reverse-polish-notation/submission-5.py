class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                second = s.pop()
                first = s.pop()
                if i == '+':
                    s.append(first + second)
                elif i == '-':
                    s.append(first - second)
                elif i == '*':
                    s.append(first * second)
                elif i == '/':
                    s.append(int(first / second))
            else: s.append(int(i))
        return s[-1]
                    
                        