class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) == len(t)):
            p1={}
            p2={}
            for i in range(len(s)):
                if s[i] in p1:
                    p1[s[i]] += 1
                else:
                    p1[s[i]] = 1
                if t[i] in p2:
                    p2[t[i]] += 1
                else:
                    p2[t[i]] = 1
            if p1 == p2:
                return True
            else:
                return False

        else:
            return False