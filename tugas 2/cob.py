n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
            a.append(int(input()))
           # a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))
