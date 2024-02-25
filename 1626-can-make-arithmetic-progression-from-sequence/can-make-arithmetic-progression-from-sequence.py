class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        print(arr)
        a=arr[1]-arr[0]
        print(a)
        for i in range(1,len(arr)-1):
            if arr[i+1]-arr[i]!=a:
                return False
        return True
             