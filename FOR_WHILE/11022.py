# 20220627 정채윤 백준 11022번

import sys

if __name__=="__main__":
    T = int(input())

    for i in range(T):
        A, B = map(int, sys.stdin.readline().split())
        print("Case #%d: %d + %d =" %(i + 1, A, B), A + B)
    
