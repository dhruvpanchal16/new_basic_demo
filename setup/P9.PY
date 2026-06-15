def alphapat(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            print(chr(num), end=" ")
        num += 1
        print("\r")

alphapat(5)