# cd = {
#     1 : (0, 128, 0), #green
#     2 : (0, 0, 255), #blue
#     3 : (255, 255, 0), #yello
#     4 : (128, 128, 128), #grey
# }
# colors = list(cd.items())
# print(colors)
# def a ():
#     cd[1] = "hello"
#     print(cd)


# for i in range(5):
#     print (i )
grid_size = [20,13]
    
lt = [] #构建一个空列表用于装载要输出的数据
for row in range(grid_size[1]): #遍历每行
    lt.append([]) #在每行中再构建一个新列表用于装载每行的数据
    for col in range(grid_size[0]): #遍历每列
        lt[row].append(str([row*grid_size[0] + col]) + " ") #将la列表中的数据添加到lt列表的对应位置


print (lt[2])