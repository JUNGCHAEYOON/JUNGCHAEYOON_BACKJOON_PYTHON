# 20220628 정채윤 백준 2562번

if __name__=="__main__":
    arr = []
    for index in range(9):
        N = int(input())
        arr.append(N)
    print(max(arr))

    for index in range(9):
        if(arr[index] == max(arr)):
            print(index + 1)