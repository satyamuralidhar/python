'''
formula:
-------- 
πr2h cubic units

about: 
For any cylinder with base radius ‘r’, and height ‘h’, the volume will be base times the height.
Therefore, the cylinder’s volume of base radius ‘r’, and height ‘h’ = (area of base) × height of the cylinder
Since the  base is the circle, it can be written as
Volume =  πr2 × h
Therefore, the volume of a cylinder = πr2h cubic units.
'''
import math 
import argparse

parser = argparse.ArgumentParser(description="Volume of Cylinder")
parser.add_argument('-R',"--radius",type=int,required=True,metavar='',help='Value of Radius')
parser.add_argument('-H',"--hight",type=int,required=True,metavar='',help='Value of Hight')

group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action='store_true',help="Print Quiet")
group.add_argument('-v','--verbose',action='store_true',help="Print Verbose")

result = None
def Cylinder(radius,hight):
    result = (math.pi) * (radius ** 2) * (hight)
    return result

#parsing the args
args = parser.parse_args()


if __name__ == "__main__":
    volume = Cylinder(args.radius,args.hight)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print("Volume of Cylinder hight {} and Radius {} and Result is {}: ".format(args.hight,args.radius,volume))
    else:
        print("Volume of Cylinder is: {}".format(volume))

'''
python argparser/volume_of_cylinder.py -R=10 -H=20
o/p: Volume of Cylinder is: 6283.185307179587
python argparser/volume_of_cylinder.py -R=10 -H=20 -v
o/p: Volume of Cylinder hight 20 and Radius 10 and Result is 6283.185307179587:
'''
