class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        for i in range(len(s)):
            if s[i].lower() == s[len(s)-1 - i].lower():
                continue
            
            else:
                return False
        return True