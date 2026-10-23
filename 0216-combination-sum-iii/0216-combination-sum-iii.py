class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        def backtrack(last,subset,total):  
            if total==n and len(subset)==k:
                result.append(subset.copy())
                return
            if total>n or len(subset)>k:
                return

            for i in range(last,10):
                sum=total+i
                subset.append(i)
                backtrack(i+1,subset,sum)
                subset.pop()

        backtrack(1,[],0)
        return result

