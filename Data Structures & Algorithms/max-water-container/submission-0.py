class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        f = 0
        r = len(heights) - 1
        while f < r:
            area = max(area, (r - f) * min(heights[f], heights[r]))
            if heights[f] < heights[r]:
                f += 1
            else:
                r -= 1
        return area