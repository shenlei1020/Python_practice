# -*- coding: utf-8 -*-
class Solution:
    def __init__(self):
        __status = 1

    def convertstr(self, s):
        """
        :param s: e.g. abcd
        :return: e.g. #a#b#c#d#
        """
        lens = len(s)
        ss = ""
        for i in range(lens):
            ss = ss + "#" + s[i]
        ss += "#"
        return ss


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        mxmid = 0
        mxright = 0
        ss = Solution.convertstr(None, s)
        lenss = len(ss)
        p = lenss*[1]
        for i in range(1, lenss):
            if mxright > i:
                p[i] = min(p[2 * mxmid - i], mxright - i)
            while i+p[i] < lenss and i-p[i] >= 0 and ss[i + p[i]] == ss[i - p[i]]:
                p[i] += 1
            if p[i] + i > mxright:
                mxmid = i
                mxright = p[i] + i
        mx = max(p)
        mxindex = p.index(mx)
        result = ss[(mxindex - mx+2):(mxindex+mx):2]
        return result


if __name__ == "__main__":
    result = Solution.longestPalindrome(None,"shdbdhjhdbfjdjdhfdhfsgfabcdefghgfedcbadksdhxskdjsdksdhskdshfdskdhcsd")
    print(result)
