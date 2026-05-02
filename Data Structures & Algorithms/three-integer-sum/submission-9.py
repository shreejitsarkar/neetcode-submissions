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
        # This would keep it O(n^2) because set lookups are O(1)
        a = set()
        for triplet in l:
            a.add(tuple(sorted(triplet))) 
        return [list(t) for t in a]

        
        