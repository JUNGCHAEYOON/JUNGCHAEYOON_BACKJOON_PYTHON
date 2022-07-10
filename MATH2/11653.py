# 20220710 정채윤 백준 11653번

if __name__=="__main__":
    X = int(input())

    while X != 1:
        for I in range(2, X + 1):
            if(X % I == 0):
                X = int(X / I)
                print(I)
                break
