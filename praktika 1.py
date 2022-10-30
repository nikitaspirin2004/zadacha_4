'''N = 5
Z = [[1,2],[3,4],[3,1],[3,7],[4,1]]
K = [[3,2],[1,1],[2,4],[3,6],[1,5]]
for i in range (N):
    kz = []
    for k in range (N):
        rx = abs(Z[i][0] - K[k][0])
        ry = abs(Z[i][1] - K[k][1])
        r = (rx**2 + ry**2)**0.5
        kz.append(r)
    coirier = kz.index(min(kz))
    print ('Заказ №',i+1,'заберет',coirier+1,"курьер.")'''



