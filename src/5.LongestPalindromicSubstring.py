class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        head = 0
        w = 1 # width of the string 
        for i in range(len(s)):
            
            if i-w>=1 and s[i-w-1:i+1]==s[i-w-1:i+1][::-1]:
                head=i-w-1
                w+=2
                continue
                
            if i-w>=0 and s[i-w:i+1]==s[i-w:i+1][::-1]:
                head=i-w
                w+=1

        return s[head:head+w]

    def longestPalindrome_(self, s: str) -> str:

        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]