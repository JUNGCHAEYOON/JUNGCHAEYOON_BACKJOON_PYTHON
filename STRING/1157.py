# 20220628 정채윤 백준 1157번

if __name__=="__main__":
    X = input().lower()         # Mississipi -> mississipi  baaa
    X_list = list(set(X))       # ['m', 'i', 's', 'p']      ['b', 'a']
    cnt = []

    for v in X_list:
        cnt_char = X.count(v)
        cnt.append(cnt_char)    # [1, 4, 4, 1]              [1, 3]

    if(cnt.count(max(cnt)) > 1):# 2                         1
        print("?")  
    else:
        A = max(cnt)                                        # 3
        B = cnt.index(A)                                    # 1
        C = X_list[B]                                       # 'a'
        D = C.upper()                                       # 'A'

        print(D)    
        # print(X_list[(cnt.index(max(cnt)))].upper())
        # lower, upper, set, append, count, index

'''
내가 직접짠 막코드

if __name__=="__main__":
    X = input()
    X = X.lower()

    dic = {}

    for c in X:
        dic[c] = 0
    
    for c in X:
        dic[c] += 1

    maxi = 0
    for key in dic:
        if(dic[key] > maxi):
            maxi = dic[key]

    samecount = 0
    for key in dic:
        if(dic[key] == maxi):
            samecount += 1
    
    if(samecount == 1):
        for key in dic:
            if(dic[key] == maxi):
                print(str(key).upper())
    else:
        print("?")

'''