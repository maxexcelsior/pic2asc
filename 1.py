cd = {
    0 : (255, 255, 255), #一般道路
    1 : (255, 234, 0), #地块
    2 : (0, 34, 255), #主次干道
    3 : (0, 255, 0), #周边绿地
    4 : (255, 0, 0), #主校园主路径
    5 : (123, 54, 8), #绿廊
    6 : (0, 0, 0) #其他用地
}


colors = list(cd.items())

print (colors)

key = 0
min_key = 0
min_dist = float("inf") #正负无穷
for col in colors:
    print(col)
    # 三维空间两点距离计算公式 (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    # + (z1 - z2) * (z1 - z2)，这里只需要比较大小，所以无需求平方根值
    # dist = (pow((col[1][0] - input_avg[0]), 2) +
    #         pow((col[1][1] - input_avg[1]), 2) +
    #         pow((col[1][2]- input_avg[2]), 2))
    # if dist < min_dist:  #所有数都比正无穷小，这里相当于获取颜色距离值列表的最小值
    #     min_dist = dist  
    #     min_key = key
    # key += 1