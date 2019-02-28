#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    
    def aplusb(self, a, b):
        # write your code here
        if (b == 0) :
            return a
        return Solution.aplusb(self,a^b,(a&b)<<1)

if __name__ == '__main__' :
    Solu=Solution()
    print(Solu.aplusb(6,-3))