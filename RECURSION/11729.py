# 20220712 정채윤 백준 11729번

def hanoi(N, start, end):
    if(N == 1):
        print(start, end)
        return
    hanoi(N - 1, start, 6 - start - end)
    print(start, end)
    hanoi(N - 1, 6 - start - end, end)
    

if __name__=="__main__":
    N = int(input())

    print(2 ** N - 1)
    hanoi(N, 1, 3)