#Eduardo Nunes
def conta(n,list):
    count = 0
    for x in list:
        if x < n:
            count +=1
    return count
print(conta(5,[1,2,3,4,4,5,6,7,8,9]))