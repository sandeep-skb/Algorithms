
class Solution(object):
    def longestPalindrome(self, s):
        res = ''
        max_len = 0
        n = len(s)
        DP = [[0] * n for _ in range(n)]
        for i in range(n):
            DP[i][i] = True
            max_len = 1
            res = s[i]
        for i in range(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                res = s[i:i+2]
                max_len = 2
        # Checking for palindromes from 0..j where j ranges from 0..n
        # doing bottom up solution
        for j in range(2, n):
            for i in range(0, j-1):
                if s[i] == s[j] and DP[i+1][j-1]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        res = s[i:j+1]
                        max_len = j - i + 1
        return res
       
sol = Solution()
sol.longestPalindrome("abba")
