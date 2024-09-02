class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon={"b":1,"a":1,"l":2,"o":2,"n":1}
        count=0
        counter = {}
        dict1={}
        a="ballon"

        if len(text)<6:
            return 0

        for i in text:
            if i in counter:
                counter[i]+= 1
            else:
                counter[i] = 1
        print("counter",counter)  

        for i in counter:
            if i in ballon:
                dict1[i] = counter[i]
        print("dict1 before normalising",dict1)

        for i in dict1:
            if i == 'l' or i == 'o':
                dict1[i] = dict1[i]//2
        print("after",dict1)

        min1=float('inf')
        for i in dict1:
            
            if dict1[i]<min1:
                print("hi")
                min1=dict1[i]
        return min1
        


        # for i in text:
        #     print(i)
        #     print("len",ballon)
        #     if len(ballon)==0:
        #         ballon = {"b":1,"a":1,"l":2,"o":2,"n":1}
        #         count+=1
        #     if i in ballon and ballon[i] == 1:
        #         del ballon[i]
        #         print("del",ballon)
        #     elif i in ballon and ballon[i]!=0:
        #         ballon[i]-=1
        #         print("val", ballon)
        # if len(ballon)==0:
        #         ballon = {"b":1,"a":1,"l":2,"o":2,"n":1}
        #         count+=1
        # return count
        
        