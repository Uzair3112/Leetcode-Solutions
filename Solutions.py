#565-Array Nesting
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if nums[x] == -1:
                continue
            count = 0
            while nums[x] != -1:
                count += 1
                nums[x], x = -1, nums[x]
            ans = max(count,ans)
        return ans

#944- Delete Columns to make sorted
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in range(len(strs[0])):
            cur = ""
            for j in range(len(strs)):
                cur += strs[j][i]
            l = list(cur)
            if l != sorted(l):
                ans += 1
        return ans
