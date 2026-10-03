class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        index = -1
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                if index != -1:
                    return [0] * len(nums)
                index = i
            else:
                prod *= nums[i]
        if index == -1:
            return_array = []
            for num in nums:
                return_array.append(int(prod/num))
            return return_array
        else:
            return_array = [0] * len(nums)
            return_array[index] = prod
            return return_array
        