# 20220629 정채윤 백준 5622번

if __name__=="__main__":
    ARR = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    S = input()
    T = 0
    
    for index1 in range(len(S)):
        for index2 in ARR:
            if(S[index1] in index2):
                T += ARR.index(index2) + 3
    
    print(T)

'''
if __name__=="__main__":
    S = str(input())

    T = 0
    for i in S:
        A = ord(i)
        if(A >=65 and A <= 67):
            T += 3
        elif(A >= 68 and A <= 70):
            T += 4
        elif(A >= 71 and A <= 73):
            T += 5
        elif(A >= 74 and A <= 76):
            T += 6
        elif(A >= 77 and A <= 79):
            T += 7
        elif(A >= 80 and A <= 83):
            T += 8
        elif(A >= 84 and A <= 86):
            T += 9
        elif(A >= 87 and A <= 91):
            T += 10
        
    print(T)
'''