class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res=[]
        def dfs(i,path):
            if sum(path)==target:
                res.append(path)   
                return
            if sum(path)> target or i==len(candidates):
                return 
            # include nums[i]
            dfs(i,path+[candidates[i]])

            # do not include
            dfs(i+1,path)

        dfs(0,path)
        return res
