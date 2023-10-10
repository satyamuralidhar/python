'''
The volume of a cone = (1/3) πr2h cubic units
‘r’ is the base radius of the cone

‘l’ is the slant height of a cone

‘h’ is the height  of the cone

As we can see from the above cone formula, the capacity of a cone is one-third of the capacity of the cylinder. That means if we take 1/3rd of the volume of the cylinder, we get the formula for cone volume
'''

import argparse
import math

parser = argparse.ArgumentParser("Volume Of The Cone")

parser.add_argument('-R','--radius',type=int,metavar='',help='Value Of Radius')
parser.add_argument('-H','--hight',type=int,metavar='',help='Value Of Hight')



group = parser.add_mutually_exclusive_group()

group.add_argument('-c','--cone',help="Cone",action='store_true')
group.add_argument('-v','--verbose',help="verbose",action='store_true')

args = parser.parse_args()

result = None
def Volume_Of_Cone(radius,hight):
    result = (1/3) * (math.pi) * (radius**2) * hight
    return result

if __name__ == "__main__":
    volume = Volume_Of_Cone(args.radius,args.hight)
    if args.verbose:
        print("Hight is {} Radius is {}: Volume Of The Cone is {}".format(args.hight,args.radius,volume))
    else:
        print("Volume Of The Cone: {}".format(volume))



