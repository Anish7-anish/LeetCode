class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i == "+":
                a = stk.pop()
                b = stk.pop()
                stk.append(a+b)
            elif i == "-":
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
            elif i == "*":
                a = stk.pop()
                b = stk.pop()
                stk.append(a*b)
            elif i == "/":
                a = stk.pop()
                b = stk.pop()
                if a!=0:
                    stk.append(int(b/a))
            else:
                stk.append(int(i))
        return stk[-1]
        

