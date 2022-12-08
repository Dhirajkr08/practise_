x =   [[1,2,3],
       [14,16,18],
       [4,6,8]]

y = [[14,54,12],
      [16,4,7],
      [12,6,9]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
        for r in result:
            print(r)
