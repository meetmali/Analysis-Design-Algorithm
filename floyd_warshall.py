V = 4
INF = 999


def floyd_warshall(G):
    distance = [[j for j in i] for i in G]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    print_solution(distance)


def print_solution(distance):
    for i in range(V):
        for j in range(V):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
     [2, 0, INF, 4],
     [INF, 1, 0, INF],
     [INF, INF, 2, 0]]

floyd_warshall(G)