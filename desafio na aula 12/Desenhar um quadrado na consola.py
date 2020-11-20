def codigo(SIZE):
    for x in range(SIZE):
        for y in range(SIZE):
            if x == 0 or y == 0 or x == SIZE-1 or y == SIZE-1 or y == SIZE-x-1 or y == x:
                print(" * ", end="")
            else:
                print("   ", end="")
        print()

codigo(9)
