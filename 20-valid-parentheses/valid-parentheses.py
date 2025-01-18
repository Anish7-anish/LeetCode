class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stk.append(i)
            elif i == "}":
                if stk and stk[-1]=="{":
                    stk.pop()
                else:
                    return False
            elif i == "]":
                if stk and stk[-1]=="[":
                    stk.pop()
                else:
                    return False
            elif i == ")":
                if stk and stk[-1]=="(":
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        return True

        