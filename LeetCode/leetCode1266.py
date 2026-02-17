points = [[1,1],[3,4],[-1,0]]

time = 0 
for i in range(len(points)-1):
    x1 = points[i][0]
    y1 = points[i][1]

    x2 = points[i+1][0]
    y2 = points[i+1][1]

    dx = abs(x1-x2)
    dy = abs(y1-y2)

    next_point = max(dx, dy)

    time+=next_point

print(f"Total time taken start point to end poiont: {time}")