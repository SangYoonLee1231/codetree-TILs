n = int(input())
numbers = list(map(int, input().split()))


def get_gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a


def get_lcd(a, b):
    gcd = get_gcd(a, b)
    return a * b // gcd


def lcd(curr_n):
    global answer

    if curr_n == n:
        return

    answer = get_lcd(answer, numbers[curr_n])
    lcd(curr_n + 1)
    

answer = numbers[0]
lcd(1)

print(answer)

# lcd = a * b / gcd