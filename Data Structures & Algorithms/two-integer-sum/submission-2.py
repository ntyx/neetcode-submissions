class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for j in range(len(nums)):
            a[nums[j]] = j
        for i in range(len(nums)):
          if (target - nums[i]) in a and i != a.get(target-nums[i]):
            return [i, a.get(target-nums[i])]