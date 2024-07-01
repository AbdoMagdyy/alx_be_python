rows = int(input('Enter the size of the pattern:'))
i = 1
while i <= rows:
    n = 1
    while n <= rows:
        print("*", end="")
        n = n + 1
    print()
    i = i +1