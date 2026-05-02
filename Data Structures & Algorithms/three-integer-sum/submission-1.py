class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
       
        l=[]
        for i in range(len(nums)):
            j, r = i + 1, len(nums) - 1
            while r>j:
                if nums[r]+nums[j]==-nums[i]:
                    
                    l.append([nums[r],nums[j],nums[i]])
                    j+=1
                    r-=1
                elif nums[r]+nums[j]<-nums[i]:
                    j+=1
                else:
                    r-=1
        a=[]
        for i in l:
            if i not in a:
                a.append(i)
        return a
        