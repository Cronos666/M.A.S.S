import balls

def impData(filename):
    objects=[]
    try:
        with open(filename,'r') as data:
            for line in data:
                x=line.split(';')
                objects.append(balls.Ball(float(x[0]), float(x[1]), [float(x[2]),float(x[3]),float(x[4])], [float(x[5]),float(x[6]),float(x[7])]))
    except FileNotFoundError:
        print("File not found")
    return objects

a=impData("interstellarballs.csv")
print(a[0].getPos(),4*a[1].getMass())
