class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l=[]
        s=[]
        for i in num1:
            l.append(ord(i)-48)
        for j in num2:
            s.append(ord(j)-48)

        print(l)
        print(s)

        
        result = 0
        for digit in l:
            result = result * 10 + digit
        k=0
        for digit in s:
            k = k * 10 + digit
        return str(k*result)

        
        