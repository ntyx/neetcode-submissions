class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        res = []
        spec = 1
        zero_count = 0
        for i in range(len(nums)):
            integer = int(nums[i])
            if integer == 0:
                zero_count += 1
                continue
            total = total * integer
        copy = total
        for a in range(len(nums)):
            if nums[a] == 0:
                if zero_count > 1:
                    res.append(0)
                else:
                    res.append(copy)
            elif zero_count >= 1:
                res.append(0)
            else:
                res.append(int(copy//nums[a]))
        return res