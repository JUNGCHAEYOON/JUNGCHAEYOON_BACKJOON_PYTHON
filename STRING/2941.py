# 20220629 정채윤 백준 2941번

if __name__=="__main__":
    W = str(input())

    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for I in croatia:
        W = W.replace(I, "*")
    
    print(len(W))