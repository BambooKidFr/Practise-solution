# https://leetcode.com/problems/longest-substring-without-repeating-characters
# Given a string,
# find the length of the longest substring without repeating characters.\
class Solution:
    def leghthOfTheLongestSubstring(self, s):
        """

        :typem s: str
        :rtype: int
        """
        last_seen = {}  # mapping from character to its last seen index in s
        start = 0  # start index of current substring
        longest = 0
        for i, c in enumerate(s):
            if c in last_seen and last_seen[c] >= start:
                start = last_seen[c]+1
            else:
                longest = max(longest, i-start+1)
            last_seen[c] = i    # update the last sighting index
        return longest

a= Solution().leghthOfTheLongestSubstring('manhha')
print(a)