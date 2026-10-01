from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for i in nums:
            seen[i] += 1
        sorted_seen = dict(sorted(seen.items(), key=itemgetter(1), reverse=True))
        return list(sorted_seen.keys())[:k]