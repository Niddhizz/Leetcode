class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        mx_p=0
        while r<len(prices):
            if prices[l]<prices[r]:
                max_profit=prices[r]-prices[l]
                mx_p=max(mx_p,max_profit)
            else:
                l=r
            r+=1    
        return mx_p        
                
            