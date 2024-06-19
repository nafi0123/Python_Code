class Solution:
    def is_integar(self,s):
        if s=="":
            return False
        if s[0]=="+" or s[0]=="-":
            s=s[1:]
        return s.isnumeric()
    def is_decimal(self,s):
        if s=="":
            return False
        if s[0]=="+" or s[0]=="-":
            s=s[1:]
        part=s.split(".")

        if len(part)!=2:
            return False

        if part[0]=="":
            return part[1].isnumeric()
        if part[1]=="":
            return part[0].isnumeric()
        return part[0].isnumeric() and part[1].isnumeric()
    

    def isNumber(self, s: str) -> bool:
        s=s.strip()
        if s =="":
            return False
        s=s.lower()
        e_count=0
        for ch in s:
            if ch == "e":
                e_count+=1
                continue
            if ch not in "0123456789+-.":
                return False
        if e_count>1:
            return False
        parts=s.split("e")

        if len(parts) == 1:
            s=parts[0]
            if self.is_decimal(s) or self.is_integar(s):
                return True
            return False
        elif len(parts)==2:
            s1=parts[0]
            s2=parts[1]

            if  self.is_decimal(s1) or self.is_integar(s1) :
                if self.is_integar(s2):
                    return True
                else:
                    return False
            else:
                return False
        return True
s=Solution()
print(s.isNumber(input()))

#Time Complexity: O(n)
# Space Complexity:O(n)
