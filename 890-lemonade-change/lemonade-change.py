class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5=0
        count_10=0
        count_20=0

        for i in bills:
            if i==5:
                count_5+=1
            elif i==10 and count_5>=1:
                count_10+=1
                count_5-=1
            elif i==20 and (count_5>=1 and count_10>=1) or count_5>=3:
                count_20+=1
                if (count_5>=1 and count_10>=1):
                    count_10-=1
                    count_5-=1
                else:
                    count_5-=3
            else:
                return False
        return True

        


            
        