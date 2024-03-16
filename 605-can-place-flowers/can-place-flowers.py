class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # c=0
        # j=0
        # if flowerbed[0]==1:
        #     for i in range(0,len(flowerbed),2):
        #         print(i)
        #         if flowerbed[i]==0:
        #             c+=1
        #     if c>=n:
        #         return True
        #     else:
        #         return False
        # else:
        #     for i in range(1,len(flowerbed),2):
        #         print(i)
        #         if flowerbed[i]==0:
        #             j+=1
        #     if j>=n:
        #         return True
        #     else:
        #         return False
        c=0
        if len(flowerbed)==1 and flowerbed[0]==0 and n<=1:
            return True
        elif len(flowerbed)==1 and flowerbed[0]==1 and n>0:
            return False
            


        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i]==0:
                if flowerbed[i+1]==0:
                    c+=1
                    flowerbed[i]=1
            elif i==len(flowerbed)-1 and flowerbed[i]==0:
                if flowerbed[i-1]==0:
                    c+=1
                    flowerbed[i]=1
            elif flowerbed[i]==0 and (flowerbed[i-1]==0 and flowerbed[i+1]==0):
                c+=1
                flowerbed[i]=1
            
        return True if c>=n else False
                
            
                


        
        