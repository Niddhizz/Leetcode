class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        res=[]
        if len(nums)==0:
            return []
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[j-1]+1==nums[j]:
                    j+=1
                else:
                    break
            if (j-i)==1:
              res.append(str(nums[i]))
            else:
              res.append(str(nums[i])+'->'+str(nums[j-1]))
            i=j
        return res    
        