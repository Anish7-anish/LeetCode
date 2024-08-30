class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum1=dict1[s[0]]
        for i in range(1,len(s)):  
            if (s[i] == 'V' or s[i] == 'X' )and s[i-1]=='I':
                sum1 = sum1 - dict1[s[i-1]] + (dict1[s[i]] - dict1[s[i-1]])
                print(sum1)
            elif (s[i] == 'L' or s[i] == 'C' )and s[i-1]=='X':
                sum1 = sum1 - dict1[s[i-1]] + (dict1[s[i]] - dict1[s[i-1]])
                print(sum1)
            elif (s[i] == 'D' or s[i] == 'M' )and s[i-1]=='C':
                sum1 = sum1 - dict1[s[i-1]] + (dict1[s[i]] - dict1[s[i-1]])
                print(sum1)
            else:
                sum1 += dict1[s[i]]
        return sum1

        