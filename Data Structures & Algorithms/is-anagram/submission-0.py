class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1={}
        c2={}
        for char in s:
            if char in c1:
                c1[char]+=1
            else:
                c1[char]=1
        for char2 in t:
            if char2 in c2:
                c2[char2]+=1
            else:
                c2[char2]=1
        if c1==c2:
            return True
        elif c1!=c2:
            return False

