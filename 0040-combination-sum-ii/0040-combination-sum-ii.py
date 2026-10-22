class Solution:
    def combinationSum2(self, candidates: list[int], target: [int] )-> list[list[int]]:
        candidates.sort()
        result=[]
        subset=[]

        def backtrack(start,remain):
            if remain==0:
                result.append(subset.copy())
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>remain:
                    break
                subset.append(candidates[i])
                backtrack(i+1,remain-candidates[i])
                subset.pop()

        backtrack(0,target)
        return result


        