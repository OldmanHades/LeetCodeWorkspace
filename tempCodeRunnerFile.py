class Solution:
    def punishmentNumber(self, n: int) -> int:

        def parition(i, cur: int, target: int, string: str):
            if i == len(string) and cur == target:
                return True
            for j in range(i, len(string)):
                string[i:j+1]
                if parition(j +1, cur + int(string[i:j+1]), target, string):
                    return True
            return False
        res = 0

        for i in range(1, n + 1):
            if partition(0,0,i, str(i*i)):
                res += i * i
        return res

n = 10
Solution().punishmentNumber(n)