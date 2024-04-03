class Solution:
    def singleNumber(self, nums):
        answer = 0
        for num in nums:
            answer ^= num
        return answer
ob=Solution()
print(ob.singleNumber([4,1,2,1,2]))
