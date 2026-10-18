class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()  # sorting lets us stop early

        def backtrack(start: int, remaining: int, path: list[int]):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # all later numbers are larger, so prune
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)  # i, not i+1: reuse allowed
                path.pop()

        backtrack(0, target, [])
        return result