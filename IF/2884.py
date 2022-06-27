# 20220627 정채윤 백준 2884번

def before45(_H, _M):
    if(_M >= 45):
        print(_H, _M - 45)
    else:
        if(_H != 0):
            print(_H - 1, _M + 15 )
        else:
            print(23, _M + 15 )

if __name__ == "__main__":
    H, M = map(int, input().split())

    before45(H, M)