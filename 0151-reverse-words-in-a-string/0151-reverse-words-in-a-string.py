class Solution:
    def reverseWords(self, s: str) -> str:
        ans=[]
        temp=''
        for i in range(len(s)):
            if s[i]!=' ':
                temp+=s[i]
            elif temp!='':
                ans.append(temp)  
                temp=''
        if temp!='':
            ans.append(temp)
        return ' '.join(ans[::-1])    