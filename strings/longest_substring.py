class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #This is a sliding window technique
        index_tracker = {}
        start = max_len = 0
        for idx, val in enumerate(s):
            if val in index_tracker:
                if index_tracker[val]+1 > start:
                    start = index_tracker[val]+1
            
            cur_len = idx - start + 1
            if max_len < cur_len:
                max_len = cur_len
            index_tracker[val] = idx
            
        return max_len
 
 
 sol = Solution()
 print("Length of the longest substring: ", sol.lengthOfLongestSubstring("abcdabcdefgh"))
