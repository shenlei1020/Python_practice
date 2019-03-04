class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lens = len(s)
        if numRows == 1 or lens <= numRows:
            return s
        L = 2 * (numRows - 1)
        result = ""
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                result += s[j::L]
            else:
                j = i
                while j < lens:
                    result += s[j]
                    if j + L - 2 * i < lens:
                        result += s[j + L - 2 * i]
                    j += L
        return result


if __name__ == "__main__":
    s = "paypalishiring"
    print(Solution.convert(None, s, 4))
