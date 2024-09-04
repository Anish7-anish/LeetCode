class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        l=len(s)

        for i in range(l):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            else:
                if not len(stack):
                    return False
                p=stack.pop()
                if s[i]==')' and not p=='(':
                    return False
                elif s[i]=='}' and not p=='{':
                    return False
                elif s[i]==']' and not p=='[':
                    return False
        if len(stack):
            return False
        else:
            return True