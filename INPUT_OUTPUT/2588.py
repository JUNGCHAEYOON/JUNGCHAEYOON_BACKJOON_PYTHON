# 20220627 정채윤 백준 2588번

A = int(input())
B = int(input())
tmpB = B

while(True):
    print(A * (tmpB % 10))
    tmpB = tmpB // 10
    if(tmpB == 0):
        print(A * B)
        break

