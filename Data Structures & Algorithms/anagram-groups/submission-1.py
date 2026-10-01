class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            if tuple(sorted(s)) in seen:
                seen[tuple(sorted(s))].append(s)
            else:
                seen[tuple(sorted(s))] = []
                seen[tuple(sorted(s))].append(s)
        output = []
        for key in seen:
            output.append(seen[key])
        return output
        