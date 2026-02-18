from math import pi

# asks for radius
rad = float(input("Enter a radius: "))

#calculates diameter
diam = 2*rad

#calculates volume
vol = 4/3 * (pi*(rad**3))

#calculates circumference
circ = 2*pi*rad

#calculates surface area
surfArea = 4*pi*rad**2

print("The radius is: " + str(rad))
print("The volume is :"+ str(vol))
print("The circumference is :"+str(circ))
print("The surface area is: " + str(surfArea))