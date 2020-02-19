cd = {
    1 : (0, 128, 0), #green
    2 : (0, 0, 255), #blue
    3 : (255, 255, 0), #yello
    4 : (128, 128, 128), #grey
}
colors = list(cd.items())
print(colors)
def a ():
    cd[1] = "hello"
    print(cd)

a()
