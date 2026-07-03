class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''
        for l in s:
            if l.isalnum():
                ns += l.lower()
        if ns == ns[::-1]:
            return True
        return False