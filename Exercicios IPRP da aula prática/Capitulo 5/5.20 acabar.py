#Eduardo Nunes
def check(seq):
    for x in seq:
        print(x)
        if seq[0] != 1 or seq[1] != 1:
            print("sdkamd")
            return False
        elif seq[x] != seq[x-1] + seq[x-2]:
            return False


print(check([1,1,2,3,5,8,13,21]))