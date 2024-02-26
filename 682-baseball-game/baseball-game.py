class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in operations:
            if i == "+":
                l.append(int(l[len(l)-1])+int(l[len(l)-2]))
            elif i == "D":
                l.append(int(l[len(l)-1])*2)
            elif i == "C":
                l.pop()
            else:
                l.append(int(i))
        s=0
        for i in l:
            s+=i
        return s

