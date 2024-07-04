class Solution:
    def wordPattern(self,pattern,s) :
        s=s.split(" ")
        if len(s) != len(pattern):
            return False
        h_t={}
        for i in range(len(pattern)):
            if pattern[i] not in h_t:
                if s[i] not in h_t.values():
                    h_t[pattern[i]]=s[i]
                else:
                    return False
            elif pattern[i] in h_t:
                if h_t[pattern[i]] != s[i]:
                    return False
        return True
s=Solution()
print(s.wordPattern("abba","dog dog dog dog"))
