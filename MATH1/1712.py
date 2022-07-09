# 20220630 정채윤 백준 1712번

import math

if __name__=="__main__":
    A, B, C = map(int,input().split())
    if(B >= C):
        print(-1)
    else:
        print(int(A / (C - B)) + 1)

    