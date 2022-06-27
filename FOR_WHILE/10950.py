# 20220627 정채윤 백준 10950번

if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        X, Y = map(int, input().split())
        print(X + Y)