class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s

        if len(self.s) <= 1 and len(self.s) >= 0:
            return len(self.s)
        
        char_index = {}
        start = 0
        max_length = 0

        for end in range(len(self.s)):
            char = self.s[end]
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = end
            max_length = max(max_length, end - start + 1)
            
        return max_length

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb") == 3)
print(sol.lengthOfLongestSubstring("bbbbb") == 1)
print(sol.lengthOfLongestSubstring("pwwkew") == 3)
print(sol.lengthOfLongestSubstring("") == 0)
print(sol.lengthOfLongestSubstring("dvdf") == 3)
print(sol.lengthOfLongestSubstring(" ") == 1)
print(sol.lengthOfLongestSubstring("da") == 2)
print(sol.lengthOfLongestSubstring("ohomm") == 3)
print(sol.lengthOfLongestSubstring("xxzqi") == 4)
print(sol.lengthOfLongestSubstring("ggububgvfk") == 6)
print(sol.lengthOfLongestSubstring("ciridmtxsgaryv") == 11)
print(sol.lengthOfLongestSubstring("wsslpluuwekuaxt") == 7)
print(sol.lengthOfLongestSubstring("tyjdnmdskovpicdvrrxvlvinkegzybmtcywrmbjwpglakqvchvzvshicnqdluqgwqdnceyywglwqetunotigasjqjoddgkzwpoyv") == 14)