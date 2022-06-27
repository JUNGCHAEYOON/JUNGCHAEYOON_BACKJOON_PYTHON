# 20220627 정채윤 백준 1110번

if __name__=="__main__":
    N = int(input())
    count = 0

    oriX = N // 10 # 10의 자리
    oriY = N % 10  # 1의 자리
    X = oriX
    Y = oriY
    while True:
        count += 1
        tmp = (X + Y) % 10
        X = Y
        Y = tmp
        if(X == oriX and Y == oriY):
            break

    print(count)