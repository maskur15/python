n = int(input('Enter number of node : '))
edge = int(input('Enter number of edge: '))
g = [[] * n for _ in range(n)]
def dfs(current, dest, depth):
    print(current, end=' ')
    if current == dest:
        return True
    if depth <= 0:
        return False
    for node in g[current]:
        if dfs(node, dest, depth - 1):
            return True
    return False


def iddfs(currentNode, destination, depth):
    for i in range(depth):
        if dfs(currentNode, destination, i):
            return True
    return False


if __name__ == '__main__':
    for i in range(edge):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)

    for i in range(n):
        print(i, ": ", g[i])
    iddfs(1, 3, 5)

# testcase:
# num of node:8
# edge: 6
# 1 2
# 1 3
# 2 4
# 2 5
# 5 7
# 5 6