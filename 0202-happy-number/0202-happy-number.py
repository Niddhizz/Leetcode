class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        
        while n not in s:
            s.add(n)
            n=self.square(n)
            
            if n==1:
                return True
            
        return False
    def square(self,n):
       ans=0
    
       while n:  
         n1=n%10
         n1=n1**2
         ans+=n1
         n=n//10
       return ans
        
        
        