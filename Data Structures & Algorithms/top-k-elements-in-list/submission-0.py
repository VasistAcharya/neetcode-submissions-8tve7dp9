class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        result=[]
        for j in range(k):
            maximum=max(count,key=count.get)
            result.append(maximum)
            del count[maximum]
        return result
