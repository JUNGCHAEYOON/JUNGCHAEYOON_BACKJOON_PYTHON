# 20220629 정채윤 백준 2908번

if __name__=="__main__":
    A, B = list(map(str, input().split()))

    A_list = list(A)
    B_list = list(B)
    RA_list = []
    RB_list = []    
    
    A_RI = len(A) - 1
    B_RI = len(B) - 1
    
    for _ in range(len(A)):
        RA_list.append(A_list[A_RI])
        A_RI -= 1
    
    for _ in range(len(B)):
        RB_list.append(B_list[B_RI])
        B_RI -= 1

    RA = int("".join(RA_list))
    RB = int("".join(RB_list))

    if(RA > RB):
        print(RA)
    else:
        print(RB)
    

    

