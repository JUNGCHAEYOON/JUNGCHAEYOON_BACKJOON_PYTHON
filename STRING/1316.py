# 20220629 정채윤 백준 1316번

if __name__=="__main__":
    N = int(input())

    cnt = 0
    for _ in range(N):
        S = input()

        arr = []
        isGroup = True
        for i in range(len(S)):
            if(i == len(S) - 1):
                if(arr.count(S[i]) == 0):
                    arr.append(S[i])
                else:
                    isGroup = False
            elif(S[i] != S[i + 1]):
                if(arr.count(S[i]) == 0):
                    arr.append(S[i])
                else:
                    isGroup = False
        if isGroup:
            cnt += 1
            
    print(cnt)
       
