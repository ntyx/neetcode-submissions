class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set()
        count = 0
        for num in nums:
            n.add(num)
        for num in n:
            if (num - 1) not in n:
                newcount = 0
                i = 0
                while True:
                    if (num + i) in n:
                        newcount += 1
                        i += 1
                    else:
                        break
                count = max(count, newcount)
            else:
                continue
        return count