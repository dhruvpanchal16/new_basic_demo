def def1(rows):
    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(i):
            if j == 0 or j == i - 1 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def1(5)