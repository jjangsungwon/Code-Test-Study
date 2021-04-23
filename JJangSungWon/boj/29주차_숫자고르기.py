import sys
sys.setrecursionlimit(10**9)


def dfs(idx, f, s, way):

    # 두 집합 일치
    cnt = 0
    for num in f:
        if num in s:
            cnt += 1
    if cnt == len(f):
        answer.update(way)
        for index in way:
            visited[index] = True

    # 두 집합 일치 x
    if second[idx] not in way:
        f.add(first[second[idx]])
        s.add(second[second[idx]])
        way.add(second[idx])
        dfs(second[idx], f, s, way)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    first = [0] + [i for i in range(1, n + 1)]
    second = [0] + [int(sys.stdin.readline()) for _ in range(n)]
    answer = set()

    # 방문 여부
    visited = [False] * (n + 1)

    # dfs
    for i in range(1, n + 1):
        dfs(i, {first[i]}, {second[i]}, {i})

    print(len(answer))
    answer = list(answer)
    answer.sort()
    for num in answer:
        print(num)