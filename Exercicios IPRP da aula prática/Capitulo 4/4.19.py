#Eduardo Nunes
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

def matrix(list):
    for lists in list:
        pos = list.index(lists)

        # método não muito bom:

        # print(f"({lists},0): {list[lists][0]}\t"
        #      f"({lists},1): {list[lists][1]}\t"
        #      f"({lists},2): {list[lists][2]}\t")

        for x in range(len(lists)):
            #print(pos, [x])
            #print(lists[x])
            print("(%1d,%1d): %2d\t" % (pos, x, lists[x]) , end="")
        print("") #dar print a somente um paragrafo
        #print("\n", end="")


matrix(list)
