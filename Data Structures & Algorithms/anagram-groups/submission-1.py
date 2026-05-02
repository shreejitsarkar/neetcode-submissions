class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newstrs=["".join(sorted(strst)) for strst in strs]
        dic={}
        for i in range(len(strs)):
            if newstrs[i] not in dic:
                dic[newstrs[i]]=[]
            dic[newstrs[i]].append(strs[i])
        return list(dic.values())