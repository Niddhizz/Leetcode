class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,total=0,0
        ans=float('inf')
        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                
                ans=min(ans,i-l+1)

                total-=nums[l]
                l+=1
                
                
        return ans if ans!=float('inf') else 0      
                