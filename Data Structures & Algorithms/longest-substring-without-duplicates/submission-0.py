class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        f, my_max = 0, 0

        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[f])
                f += 1
            my_set.add(s[r])
            my_max = max(my_max, r - f + 1)
        return my_max
        