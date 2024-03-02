n = int(input())

char = ord('A')
char_plus = 0

for i in range(n):
    print("  " * i, end="")

    for _ in range(n - i):
        print(chr(char + char_plus), end=" ")
        char_plus = (char_plus + 1) % 26
    
    print()