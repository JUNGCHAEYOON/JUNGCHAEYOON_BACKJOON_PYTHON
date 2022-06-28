# 20220628 정채윤 백준 1546번

if __name__=="__main__":
    N = int(input())
    arr = list(map(int,input().split()))

    maxi = max(arr)
    for index in range(N):
        arr[index] = (arr[index]/maxi) * 100

    print(sum(arr)/len(arr))