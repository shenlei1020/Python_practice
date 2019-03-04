class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # lens = len(s)
        lenp = len(p)
        if not (s or p):
            return True
        elif s and (not p):
            return False
        elif (not s) and p:
            if lenp % 2 == 0 and p[1::2] == (lenp//2) * "*":
                return True
            else:
                return False
        if p[-1] == s[-1] or p[-1] == ".":
            return Solution.isMatch(None, s[:-1], p[:-1])
        elif p[-1] == "*":
            if p[-2] == s[-1] or p[-2] == ".":
                return Solution.isMatch(None, s[:-1], p) or Solution.isMatch(None, s, p[:-2])
            else:
                return Solution.isMatch(None, s, p[:-2])
        else:
            return False


if __name__ == "__main__":
    s = "aaa"
    p = "ab*ac*a"
    print(Solution.isMatch(None, s, p))
