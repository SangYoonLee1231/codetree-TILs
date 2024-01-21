a, b, c, d = tuple(map(int, input().split()))

start_min = a * 60 + b * 1
end_min = c * 60 + d * 1

print(end_min - start_min)