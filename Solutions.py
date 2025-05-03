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


#38 Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:

        def convertToString(lst):
            s = ""
            for i in range(len(lst)):
                s += str(lst[i][0]) + str(lst[i][1])
            return s 

        def convertToArray(st):
            if len(st) == 1:
                new = [[1,1]]
                return convertToString(new)
            new = []
            i = 0
            while i<len(st)-1:
                ch = st[i]
                count = 1
                for j in range(i+1,len(st)):
                    if st[j] == ch:
                        count += 1
                    else:
                        break
                i += count
                new.append([count,ch])
            if len(st) > 1 and st[-1] != st[-2]:
                new.append([1,st[-1]])
                
            return convertToString(new)

        s = "1"
        for i in range(n-1):
            s = convertToArray(s)
        return s