class Solution:    

    def twoSum(self, nums, target: int):
        arr = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i == j):
                    continue
                if nums[i] + nums[j] == target:
                    arr.append(i)
                    arr.append(j)
                    return arr

        return arr

s = Solution()       
print(s.twoSum([2,7,11,15], 9))
