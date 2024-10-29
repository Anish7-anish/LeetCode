class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        a = list(s)
        n = len(s)
        i = 0

        if len(s) == 1:
            return False
        while i < n:
            if a[i] == "(" or a[i] == "{" or a[i] == "[":
                stk.append(a[i])
            elif a[i] == "}" and len(stk)>0:
                if stk[-1] == "{":
                    stk.pop()
                else:
                    return False
            elif a[i] == "]" and len(stk)>0:
                if stk[-1] == "[":
                    stk.pop()
                else:
                    return False
            elif a[i] == ")" and len(stk)>0:
                if stk[-1] == "(":
                    stk.pop()
                else:
                    return False
            else:
                return False
            i = i+1

        if len(stk) == 0:
            return True
        return False