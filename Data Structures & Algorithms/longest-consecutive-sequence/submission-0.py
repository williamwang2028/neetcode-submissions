class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        starts = {}
        toReturn = 0
        for num in nums:
            if num - 1 not in hash_set:
                current = num
                length = 1
                while current + 1 in hash_set:
                    length += 1
                    current += 1

                toReturn = max(toReturn, length)



        return toReturn
        
        