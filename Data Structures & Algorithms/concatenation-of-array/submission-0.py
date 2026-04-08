class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        j=0
        ans=[]
        for i in range(2):
            while j<len(nums):
                ans.append(nums[j])
                j+=1
            j=0
        return ans

        