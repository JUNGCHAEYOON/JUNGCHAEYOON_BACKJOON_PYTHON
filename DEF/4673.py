# 20220628 정채윤 백준 4673번

def sumAll(N):
    total = N
    for index in str(N):
        total += int(index)
    return total 
    
def selfNumber():
    arr1 = list(range(1, 10001))
    arr2 = list(range(1, 10001))
    for index in arr1:
        SA = sumAll(index)
        if(SA < 10001):
            arr2[SA - 1] = -1
        
    for index in arr2:
        if(index > 0):
            print(index)
    

if __name__=="__main__":
    selfNumber()


