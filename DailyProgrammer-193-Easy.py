#!/usr/bin/env python3
# reddit.com/r/dailyprogrammer - Challenge 193 - Easy
import math
import sys
import itertools
"""
###Description:

An international shipping company is trying to figure out how to manufacture various
types of containers. Given a volume they want to figure out the dimensions of various
shapes that would all hold the same volume.

###Input:

A volume in cubic meters.

###Output:

Dimensions of containers of various types that would hold the volume. The following containers are possible.

    Cube
    Ball (Sphere)
    Cylinder
    Cone

###Example Input:

27

###Example Output:

 Cube: 3.00m width, 3.00m, high, 3.00m tall
 Cylinder: 3.00m tall, Diameter of 3.38m
 Sphere: 1.86m Radius
 Cone: 9.00m tall, 1.69m Radius

###Some Inputs to test.

27, 42, 1000, 2197


"""

# V = width^3 = length^3 = height^3
def cube_vol(vol):
    width = length = height = vol**(1/3.0)
    return {'width' : width, 'length' : length, 'height': height}

# V = pi*radius^2*height
def cylinder_vol(vol):
    height = vol**(1/3.0)
    radius = (vol/(math.pi*height))**(1/2.0)
    return {'height' : height, 'radius' : radius}

# V = 4/3*pi*radius^3
def sphere_vol(vol):
    radius = (vol/(4.0/3.0*math.pi))**(1/3.0)
    return {'radius' : radius}

# V = height/3*pi*radius^2
# Assume height = 2*radius
def cone_vol(vol):
    radius = (vol*3/2.0/math.pi)**(1/3.0)
    height = radius*2
    return {'height' : height, 'radius' : radius}

def print_volumes(cube, cylinder, sphere, cone):
    print("Cube: {:.2f}m width,  {:.2f}m length,  {:.2f}m height".format(cube['width'], cube['length'], cube['height']))
    print("Cylinder: {:.2f}m tall, Diameter of {:.2f}".format(cylinder['height'], 2*cylinder['radius']))
    print("Sphere: {:.2f}m Radius".format(sphere['radius']))
    print("Cone: {:.2f}m tall, {:.2f}m Radius".format(cone['height'], cone['radius']))

# If an input is not given within command line
if len(sys.argv) < 2:
    print('Input volume in meters^3:')
    input = input()
    cube = cube_vol(int(input))
    cylinder = cylinder_vol(int(input))
    sphere = sphere_vol(int(input))
    cone = cone_vol(int(input))
    print_volumes(cube, cylinder, sphere, cone)
    
#If a list of volumes are given as input separated by whitespace
if len(sys.argv) >= 2:
    for volume in itertools.islice(sys.argv, 1, len(sys.argv)):
        print("Volume = " + volume)
        cube = cube_vol(int(volume))
        cylinder = cylinder_vol(int(volume))
        sphere = sphere_vol(int(volume))
        cone = cone_vol(int(volume))
        print_volumes(cube, cylinder, sphere, cone)
        print('')
