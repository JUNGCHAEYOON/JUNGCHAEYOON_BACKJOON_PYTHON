# 20220628 정채윤 백준 2577번

if __name__=="__main__":
    arr1 = []
    for index in range(10):
        N = int(input())
        arr1.append(N)

    arr2 = []
    for index in arr1: 
        if (index % 42 not in arr2):
            arr2.append(index % 42)

    print(len(arr2))