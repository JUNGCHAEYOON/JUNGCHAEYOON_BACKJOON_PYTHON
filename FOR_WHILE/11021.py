# 20220627 정채윤 백준 11021번

import sys

if __name__=="__main__":
    T = int(input())

    for i in range(T):
        A, B = map(int, sys.stdin.readline().split())
        print("Case #%d:" % (i + 1) , A + B)
    
