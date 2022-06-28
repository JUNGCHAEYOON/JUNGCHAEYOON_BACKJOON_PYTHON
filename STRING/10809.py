# 20220628 정채윤 백준 11720번

if __name__=="__main__":
    S = str(input())
    arr = []

    for _ in range(26):
        arr.append(-1)
    
    for index, value in enumerate(S):
        if(arr[ord(value) - 97] == -1):
            arr[ord(value) - 97] = index
        
    for index in arr:
        print(index, end = " ")