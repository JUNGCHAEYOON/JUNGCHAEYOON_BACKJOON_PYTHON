# 20220705 정채윤 백준 2869번

if __name__=="__main__":
    A, B, V = map(int,input().split())

    K = (V - B) / (A - B)
    print(int(K) if K == int(K) else int(K) + 1)
    
    '''
    L = 0
    date = 0
    while True:
        date += 1
        L += A
        if(L >= V):
            print(date) 
            break
        L -= B
    '''