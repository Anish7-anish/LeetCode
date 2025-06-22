class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum1 = 0

        
        
        for i in range(len(s)):
            if (s[i] == "V" or s[i] == "X") and i>0 and s[i-1] == "I":
                sum1+=(roman[s[i]]) - 2*(roman[s[i-1]])
            elif (s[i] == "L" or s[i] == "C") and i>0 and s[i-1] == "X":
                sum1+=(roman[s[i]]) - 2*(roman[s[i-1]])
            elif (s[i] == "D" or s[i] == "M") and i>0 and s[i-1] == "C":
                sum1+=(roman[s[i]]) - 2*(roman[s[i-1]])
            else:
                sum1+=roman[s[i]]
        
        return sum1