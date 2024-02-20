class Solution:
    def productExceptSelf_bruteforce(self, nums):
        res = []
        for n in range(len(nums)):
            prefix = 1
            for j in range(0, n): # prefix
                prefix *= nums[j]
            suffix = 1
            for k in range(n+1, len(nums)): # subfix
                suffix *= nums[k]
            res.append(prefix*suffix)
        return res
    
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*len(nums)
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        prodSuffix = 1
        for j in range(n-1, -1, -1):
            res[j] = res[j] * prodSuffix
            prodSuffix = prodSuffix * nums[j]
        return res

# Testing
nums = [1, 2, 3, 4]

#nums = [-1,1,0,-3,3]

#print(Solution().productExceptSelf_bruteforce(nums))

print(Solution().productExceptSelf(nums))