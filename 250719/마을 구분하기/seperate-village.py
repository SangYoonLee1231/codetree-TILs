n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [
    [False] * n
    for _ in range(n)
]

drs, dcs = [0, 0, 1, -1], [1, -1, 0, 0]

town_people_nums = []


def grid_search():
    for r in range(n):
        for c in range(n):
            if can_go(r, c):
                visited[r][c] = True
                town_people_nums.append(town_search(r, c))


def town_search(r, c):
    people_num = 1

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc

        if (can_go(nr, nc)):
            visited[nr][nc] = True
            people_num += town_search(nr, nc)

    return people_num


def can_go(r, c):
    return in_range(r, c) and not visited[r][c] and grid[r][c]


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n


def print_answer():
    grid_search()

    print(len(town_people_nums))

    town_people_nums.sort()
    for town_people_num in town_people_nums:
        print(town_people_num)


print_answer()