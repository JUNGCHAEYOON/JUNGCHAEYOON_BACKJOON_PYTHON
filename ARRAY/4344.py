# 20220628 정채윤 백준 4344번

if __name__=="__main__":
    C = int(input())

    for _ in range(C):
        arr = list(map(int,input().split()))
        del(arr[0]) # 첫 글자  삭제
        avg = sum(arr)/len(arr)

        count = 0
        for index in arr:
            if(index > avg):
                count += 1
        tmp = count/len(arr) * 100
        print("{:.3f}%".format(tmp))
