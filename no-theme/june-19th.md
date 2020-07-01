# june-19th

\10. Regular Expression Matching

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        ## dp[i][j] 表示对应string 的前i/j个能不能匹配,初始化的时候都是False

        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]

        ## Base Case 就是可以 .
        dp[0][0]=True # Two empty string are True
        ##　In this case, a* only
        for i in range(2,len(p)+1):
            if p[i-1]=='*':
                dp[0][i]=dp[0][i-2]

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.' or p[j-1] == s[i -1]:
                    ## 之前对了错了,这时就改不了
                    dp[i][j]=dp[i-1][j-1]

                elif p[j-1]=='*':
                    ## 再往前看多一步
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        dp[i][j]=dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]

                else:
                    dp[i][j]= False
        return dp[len(s)][len(p)]
```

