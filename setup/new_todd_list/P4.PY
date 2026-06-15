def inverted_full_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end="")
        print("")

inverted_full_pyramid(5)