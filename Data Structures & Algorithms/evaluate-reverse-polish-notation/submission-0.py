class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        first = 0
        second = 0
        for i in tokens:
            if i in {'+', '-', '*', '/'}:
                second = s.pop()
                first = s.pop()
                match i:
                    case '+':
                        s.append(int(first)+int(second))
                    case '-':
                        s.append(int(first)-int(second))
                    case '*':
                        s.append(int(first)*int(second))
                    case '/':
                        s.append(int(first)/int(second))
            else: s.append(int(i))
        return int(s[0])
                    
                        