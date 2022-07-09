# 20220705 정채윤 백준 1193번

if __name__=="__main__":
    X = int(input())
    
    line = 0
    end = 0
    while X > end:
        line += 1
        end += line

    diff = end - X
    if line % 2 == 0 :
        top = line - diff
        bottom = diff + 1
    else:
        top = diff + 1
        bottom = line - diff

    print("%d/%d" %(top, bottom))