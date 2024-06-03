class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if s==t:
            return True
        my_dict={}
        hset=set()
        
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]]=t[i]
                if t[i] not in hset:
                    hset.add(t[i])
                else:
                    return False
   
            else:
                if t[i] != my_dict[s[i]] :
                    return False

        return True
T=Solution()
s=input()
t=input()

print(T.isIsomorphic(s,t))

# Time Complexity =O(n)
# Space Complexity =O(n)
