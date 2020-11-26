#Eduardo Nunes
def soma(list):
    newlist =[]
    for x in range(len(list)):
        if x == 0:
            newlist.append(list[x])
        else:
            newlist.append(newlist[x-1]+list[x])
    return  newlist

print(soma([1,2,3,4,5]))
#https://codeshare.io/5QoPmx