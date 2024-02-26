class Solution:
    def romanToInt(self, s: str) -> int:
        a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        for i in range(len(s)):
            if i==0:
                sum+=a[s[i]]
            elif (s[i]=="V" or s[i]=="X") and s[i-1]=="I":
                sum = sum + (a[s[i]] - 2)
            elif (s[i]=="L" or s[i]=="C") and s[i-1]=="X":
                sum = sum + (a[s[i]] - 20)
            elif (s[i]=="D" or s[i]=="M") and s[i-1]=="C":
                sum = sum + (a[s[i]] - 200)
            else:
                sum+=a[s[i]]
        return sum
            

            
                
            
        