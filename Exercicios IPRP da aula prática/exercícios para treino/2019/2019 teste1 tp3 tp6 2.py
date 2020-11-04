def obtem_sub_cadeias(string, chari, charf):
    list = []
    list2 = []
    for x in range(len(string)):
        if string[x] == chari:
            list.append(x)
        if string[x] == charf:
            list2.append(x)
    print(list)
    print(list2)
    for i in range(len(list)):
        for j in range(len(list2)):
            if list[i]>list2[j]:
                continue
            if chari in string[list[i]+1:list2[j]+1]:
                continue
            if charf in string[list[i]+1:list2[j]]:
                continue
            print(string[list[i]:list2[j]+1])



obtem_sub_cadeias("aaa#aa#aeiou###a**dsadas**aaa#abcd*","#","*")
