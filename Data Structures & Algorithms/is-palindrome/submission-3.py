class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s.lower() if char.isalnum())
        mid=(len(s)//2)
        j=len(s)-1
        for i in range(mid):
            if s[i]!=s[j]:
                return False
            j-=1
        
        return True
