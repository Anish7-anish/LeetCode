class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while(r>l):
            if numbers[r]>0 and numbers[r]>target:
                r-=1
            else:
                break
        h={}

        for i in range(len(numbers)):
            h[numbers[i]] = i
        print(h)
        for i in range(len(numbers)):
            y=target-numbers[i]

            if y in h and h[y]!=i:
                return [min(i+1,h[y]+1),max(i+1,h[y]+1)]

