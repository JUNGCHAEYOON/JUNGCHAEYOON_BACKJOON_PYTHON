# 20220710 정채윤 백준 2447번

import sys

def star(N):
    if(N == 1):
        return ["*"]
    
    stars = star(N // 3)
    arr = []

    for i in stars:
        arr.append(i * 3)
    for i in stars:
        arr.append(i + " " * (N // 3) + i)
    for i in stars:
        arr.append(i * 3)
    
    return arr
        
        
if __name__=="__main__":
    N = int(sys.stdin.readline().strip())

    print("\n".join(star(N)))