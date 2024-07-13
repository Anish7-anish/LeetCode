class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        betters = [ord(i) for i in letters]
        print(betters)
        betters= sorted(list(set(betters)))
        print(betters)
        
        target1 = ord(target)

        if max(letters)<target:
            return letters[0]
        
        start=0
        end = len(betters)-1

        while start<=end:
            mid =(start+end)//2

            if target1 == betters[mid]:
                if mid == len(betters)-1:
                    return letters[0]
                    
                return chr(betters[mid + 1])
            elif target1>betters[mid]:
                start=mid+1
            else:
                end=mid-1
        return chr(betters[start])

        