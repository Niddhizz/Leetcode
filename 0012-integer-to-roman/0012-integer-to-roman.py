class Solution:
    def intToRoman(self,num:int)->str:
        lst=[["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],         ["D",500],["CM",900],["M",1000]]       
        ans=''
        for i,j in reversed(lst):
            if num//j:
                count=num//j
                ans+=(i*count)
                num=num%j
        return ans        
                