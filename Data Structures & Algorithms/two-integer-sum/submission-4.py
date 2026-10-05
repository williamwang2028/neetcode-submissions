class Solution:
    def twoSum(self, nums: List[int], target: int) -> List(int):
        my_dict = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in my_dict:
                return [my_dict[complement], index]
            my_dict[value] = index