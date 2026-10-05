class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res, f, maxf = 0, 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf, count[s[r]])

            while (r - f + 1) - maxf > k:
                count[s[f]] -= 1
                f += 1
            res = max(res, r - f + 1)
        
        return res

        