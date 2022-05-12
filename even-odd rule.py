
def is_point_in_path(p, poly):
    # determine if the point is in the polygon
    # return True if the point is in the path or is a corner or on the boundary
     
        x = p[0]
        y = p[1]
        num = len(poly)
        j = num - 1
        c = False
        for i in range(num):
            if (x == poly[i][0]) and (y == poly[i][1]):
                # point is a corner
                return True
            if ((poly[i][1] > y) != (poly[j][1] > y)):
                # slope = ((x - poly[i][0]) * (poly[j][1] - poly[i][1])
                #         - (poly[j][0] - poly[i][0]) * (y - poly[i][1]))

                slope = ((y - poly[i][1]) * (poly[j][0] - poly[i][0])
                        - (poly[i][1] - poly[j][1]) * (poly[i][0] - x))


                if slope == 0:
                    # point is on boundary
                    return True
                if (slope < 0) != (poly[j][1] < poly[i][1]):
                    c = not c
            j = i
        return c

# test
poly = [(1,0), (0,1), (-1,0), (0,-1)]

p = (1, 0)
if is_point_in_path(p, poly):
    print ('Yes')
else:
    print ('No')

