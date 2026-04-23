class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=[]
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
        k=len(seen)
        for i in range(k):
            nums[i] = seen[i]
        return k
