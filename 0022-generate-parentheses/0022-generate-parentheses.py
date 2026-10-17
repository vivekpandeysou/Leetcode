class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]
        bracket=n*2
        
        def solve(current,open_count,close_count):
            if len(current)==2*n:
                result.append("".join(current))
                return

            if open_count<n:
                current.append("(")
                solve(current,open_count+1,close_count)
                current.pop()

            if close_count<open_count:
                current.append(")")
                solve(current,open_count,close_count+1)
                current.pop()

        solve([],0,0)
        return result


            
        
        