class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsset = set(jewels)

        count=0
        for i in stones:
            if i in jewelsset:
                count+=1
        return count
        