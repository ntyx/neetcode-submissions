class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            dist = right - left
            vol = dist * min(heights[left], heights[right])
            max_vol = max(vol, max_vol)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else: 
                left += 1
                right -= 1
        return max_vol
