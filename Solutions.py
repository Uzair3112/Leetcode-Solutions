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

#2799. Count Complete Subarrays in an Array
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        def sub(nums):
            subs = []
            for i in range(len(nums)):
                for j in range(i,len(nums)):
                    subs.append(nums[i:j+1])
            return subs
        subarrays = sub(nums)
        ans = 0
        for i in subarrays:
            if len(set(i)) == len(set(nums)):
                ans += 1
        return ans


#2570. Merge Two 2D Arrays by Summing Values
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        n1 = len(nums1)
        n2 = len(nums2)
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i][0] == nums2[j][0]:
                ans.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                ans.append(nums1[i])
                i += 1
            else: 
                ans.append(nums2[j])
                j += 1
        while i < n1:
            ans.append(nums1[i])
            i += 1
        while j < n2:
            ans.append(nums2[j])
            j += 1
        return ans


#2094. Finding 3-Digit Even Numbers
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits = list(map(str,digits))
        import itertools
        l = list(itertools.permutations(digits,3))
        n = []
        for i in l:
            if i[0] == "0" or int(i[-1])%2 != 0:
                continue
            n.append("".join(i))
        n = set(map(int,n))
        return sorted(list(n))
