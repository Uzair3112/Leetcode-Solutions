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


#22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openP, closeP, s):
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)
                return
            
            if openP < n:
                dfs(openP + 1, closeP, s + "(")
            
            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")

        return res
    

#3356. Zero Array Transformation II
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        m=len(queries)
        # if(nums.count(0)==n):
        #     return 0
        ans=0
        currentSum=0
        diffMap=defaultdict(int)
        for i in range(n):
            currentSum+=diffMap[i]
            #print(i,currentSum)
            
            if(nums[i]==0 or currentSum+nums[i]<=0):
                continue
            
            #ans+=1
            while(currentSum+nums[i]>0 and ans<m):
                l,r,val=queries[ans]
                diffMap[l]-=val
                diffMap[r+1]+=val
                if(l<=i and r>=i):
                  currentSum-=val
                ans+=1
            if(currentSum+nums[i]>0):
                return -1
            #print(i,ans,diffMap,currentSum)
        return ans

#540. Single Element in a Sorted Array
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if mid%2 == 1:
                mid -= 1
            if nums[mid] != nums[mid+1]:
                right = mid
            else:
                left = mid+2
        return nums[left]


#1550. Three Consecutive Odds
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        t = False
        for i in range(len(arr)-2):
            if arr[i]%2 != 0 and arr[i+1]%2 != 0 and arr[i+2]%2 != 0:
                t = True
                return t
        return t

#1534. Count Good Triplets
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                for k in range(j+1,len(arr)):
                    if abs(arr[i]-arr[j]) <= a:
                        if abs(arr[j]-arr[k]) <= b:
                            if abs(arr[i]-arr[k]) <= c:
                                count += 1
        return count