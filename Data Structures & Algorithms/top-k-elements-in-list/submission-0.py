class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapset = defaultdict(int)
        ans=[]
        for num in nums:
            mapset[num] += 1
        res = sorted(mapset.items(), key=lambda item: item[1], reverse = True)
        for i in range(k):
            ans.append(res[i][0])
        return ans
