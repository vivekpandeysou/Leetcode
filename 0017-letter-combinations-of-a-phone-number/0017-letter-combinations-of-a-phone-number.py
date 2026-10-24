class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result=[]
        def backtrack(index,subset):
            if index>=len(digits):
                result.append("".join(subset))
                return
            for p in phone[digits[index]]:
                subset.append(p)
                backtrack(index+1,subset)
                subset.pop()



        backtrack(0,[])
        return result