class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            a[s[i]] = a.get(s[i], 0) + 1
        for j in range(len(t)):
            if t[j] not in a or a.get(t[j]) == 0:
                return False
            a[t[j]] -= 1
        return True
        