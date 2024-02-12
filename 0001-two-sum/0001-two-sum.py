class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
           dic={}
           for i ,val in enumerate(nums):
                dif=target-val
                if dif in dic:
                    return [dic[dif],i]
                dic[val]=i
                