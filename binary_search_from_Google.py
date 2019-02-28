#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        temp_input = input().split()
        temp_input = list(map(int, temp_input))
        NMax = int(input())
        start = temp_input[0] + 1
        end = temp_input[1]
        mid = (start + end) // 2
        print(mid)
        judge = input()
        N = 1
        while judge != "CORRECT" and N < NMax:
            if judge == "TOO_SMALL":
                start = mid + 1
            elif judge == "TOO_BIG":
                end = mid - 1
            elif judge == "WRONG_ANSWER":
                print("Wrong!")
                exit(0)
            mid = (start + end) // 2
            print(mid)
            judge = input()
            N += 1
