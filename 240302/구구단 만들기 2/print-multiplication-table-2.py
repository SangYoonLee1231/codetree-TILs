a, b = tuple(map(int, input().split()))

for i in range(1, 5):
    for j in range(b, a - 1, -1):
        print(f"{j} * {i * 2} = {j * i * 2}", end="")

        if j == a:
            break
        
        print(" / ", end="")
    
    print()