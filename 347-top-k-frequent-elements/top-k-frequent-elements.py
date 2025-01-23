class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [0]*(n+1)
        freq = {}

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        
        for key, val in freq.items():
            if buckets[val]==0:
                buckets[val] = [key]
            else:
                buckets[val].append(key)

        ret = []

        for i in range(n,-1,-1):
            if buckets[i]!=0:
                ret.extend(buckets[i])
            if len(ret)==k:
                break
        return ret
        

        



        