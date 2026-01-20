import balls
import sys

def impData(filename):
    objects=[]
    try:
        with open(filename,'r') as data:
            for line in data:
                x=line.split(';')
                objects.append(balls.Ball(float(x[0]), float(x[1]), [float(x[2]),float(x[3]),float(x[4])], [float(x[5]),float(x[6]),float(x[7])]))
    except FileNotFoundError:
        print("File not found")
        sys.exit()
    except ValueError:
        print("Wrong file fomrat")
        sys.exit()
    return objects


def expData(filename,objects):
        with open(filename,'w') as data:
            for line in objects:
                data.write(str(line.getMass())+
                           ";"+str(line.getRad())+
                           ";"+str(line.getPos()[0])+
                           ";"+str(line.getPos()[1])+
                           ";"+str(line.getPos()[2])+
                           ";"+str(line.getVel()[0])+
                           ";"+str(line.getVel()[1])+
                           ";"+str(line.getVel()[2])+
                           "\n")
