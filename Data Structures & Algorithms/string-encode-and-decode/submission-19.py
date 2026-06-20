class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        ans, i = [], 0
        while i < len(s):
            j = i
            num = ""
            while s[j] != "#":
                num += s[j]
                j += 1
            number = int(num)
            ans.append(s[j+1:number+j+1])
            i = j+number+1
        return ans
