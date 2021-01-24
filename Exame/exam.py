str1= "acegikmoqsuwyA"
str2= "bdfhjlnprtvxzBCD"
def processsa(str1,str2):
    t = []
    max1 = len(str1)
    t.append(max1)
    max2 = len(str2)
    t.append(max2)
    maxi = max(t)

    newstr = ""

    for x in range(maxi):
        if x + 1 > len(str1)-1:
            newstr += str2[x]

        elif x + 1 > len(str2)-1:
            newstr += str1[x]
        else:
            newstr += str1[x] + str2[x]

    leng = len(newstr)

    return [newstr,leng]

print(processsa(str1,str2))

list = [1,2,3,1,1,1,1]
new = set(list)


print(set(list))