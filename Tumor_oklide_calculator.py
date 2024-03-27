import math

def oklide_calculate(px, py, qx, qy):
    distance = math.sqrt((qx - px) ** 2 + (qy - py) ** 2)
    return distance

px=float(input("Enter the location x of the first tumor:"))
py=float(input("Enter the location y of the first tumor:"))
qx=float(input("Enter the location x of the second tumor:"))
qy=float(input("Enter the location y of the second tumor:"))
distance=oklide_calculate(px,py,qx,qy)
print("The distance between of the two tumors is:{}".format(distance))
