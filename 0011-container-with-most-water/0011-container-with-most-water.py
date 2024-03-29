class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        l,r=0,len(height)-1
        while l<r:
            area=min(height[l],height[r])*(r-l)
            ans=max(ans,area)
            if height[l]>height[r]:
                r-=1
            elif height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans        