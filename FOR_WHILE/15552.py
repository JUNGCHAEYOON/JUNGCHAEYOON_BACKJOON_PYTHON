# 20220627 정채윤 백준 15552번

import sys

if __name__ == "__main__":
    T = int(input())
    
    for i in range(T):
        X, Y = map(int, sys.stdin.readline().split())
        print(X + Y)