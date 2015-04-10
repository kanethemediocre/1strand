# 1strand
#An open source g-code generator for 3d printers that makes parts from a single continuous extrudate.

#Still puts the last instruction at the start.

#v002 hardcoded parameters for a 1cm square/cube
#v003 User-entered parameters for an arbitrary rectangle and printer.
#v004 Actually tested to produce a physical rectangle.  Corrected G-code syntax in final line
#v005 Added circle and tested to create physical circle.  Added untested prompt/choice for the shape.  Moved rectangle function and circle to shapes.py

#Immediate Goals:
#Perimeter following coordinates from spreadsheet
#Create objects with paths that end somewhere other than they start, but reverse the process each layer so the strand #isn't broken
#Perfect Bushing Tool
#Clone copies of objects to print sequentially.  Parallel would require extruder stoppage, which kind of defeats the #point.
#Fillet radii

#Long Term Goals:
#All kinds of printer hardware optimization/kludges
#Object creation interface
#CAD file input
#Non-planar prints

import Shapes
print "Gcode generator Alpha 0.0004"
xpath = []
ypath = []
zpath = []
step = []
epath = []
xstart = 10.0
ystart = 10.0
zstart = 0.5
LayerHeight = 0.5
ExtrusionWidth = 1.0
FilamentDiameter=1.75
MiddleMarkerX = 15.0 #This is only to determine an "inside" of a closed perimeter
MiddleMarkerY = 15.0 #Will be overridden later, but these may be used for testing
FilamentArea = FilamentDiameter * 3.14159 / 4.0
GooCoefficient = LayerHeight * ExtrusionWidth / FilamentArea
print "GooCoefficient is the amount of millimeters of filament that will be pushed per millimeter of xy travel"
print "The GooCoefficient is calculated based on parameters LayerHeight, ExtrusionWidth, and FilamentDiameter"
print "Current values are:"
print "LayerHeight =", LayerHeight
print "ExtrusionWidth=", ExtrusionWidth
print "FilamentDiameter=", FilamentDiameter
print "GooCoefficient=", GooCoefficient

Default = raw_input("Do you [Y]earn for the default settings or want to [N]itpick?")
if Default=='y' or Default == 'Y':
   print "wiggity-waaaaa"
if Default=='n' or Default=='N':
   LayerHeight=float(raw_input("LayerHeight:"))
   ExtrusionWidth=float(raw_input("ExtrusionWidth:"))
   FilamentDiameter=float(raw_input("FilamentDiameter:"))#   print 'You fail at input.'
   GooCoefficient = LayerHeight * ExtrusionWidth / FilamentArea
   print "GooCoefficient is calculated to", GooCoefficient
   GooCoefficient=float(raw_input("Override GooCoefficient or 0 to use calculated value"))
   if GooCoefficient==0:
      GooCoefficient = LayerHeight * ExtrusionWidth / FilamentArea
      print "Goo Coefficient Calculated to", GooCoefficient

#The rectangle code is in Shapes.py.  I'm trying to build a library there.

shapechoice = raw_input("[C]ircle or [R]ectangle"))
if shapechoice == 'R' or shapechoice == 'r':
   Height=Shapes.rectanglecreator(xpath,ypath,zpath)
if shapechoice == 'C' or shapechoice == 'c':
   Height = Shapes.circlecreator(xpath,ypath,zpath)







#This assumes the layer paths end where they start.
#Finding the number of steps in a layer (at this point, just 1 perimeter of a layer)
#is important for all sorts of post-processing to that shape.
StepsPerLayer=len(xpath)-1 #need to update this value to accomodate multiple perimeters
#Try assumption that inside is always the +x, Xy direction.
   


#Below is a perimeter adding function
#This is going to be complicated....
#Find the midpoint of the side, and see which is closer to the center for initial orientation.
#Center is hardcoded for now
xcenter=15.0
ycenter=15.0
#Let the first segment be defined as from x1, y1 to x2, y2
x1 = xpath[3]
x2 = xpath[4]
y1 = ypath[3]
y2 = ypath[4]
xmid = (x1+x2) / 2
ymid = (y1+y2) / 2
xdistance = x2-x1
ydistance = y2-y1
up = 0
down = 0
if x1 == x2 and y1 > y2:
   down = 1
if x1 == x2 and y2 > y1:
   up = 1
if x1 == x2 and y2 == y1:
   print "Starting segment has 0 length"
if up==0 and down==0:
   slope = ydistance / xdistance #because why not i guess...
if xpath[len(xpath)-1] == xpath[3] and ypath[len(ypath)-1] == ypath[3]: #Checking if start and end are the same point.
   print "Looping path detected."






#Below is a layer multiplying function that assumes the start
#and end are in the same place
for x in range(2, int(Height/LayerHeight)+1): #Each layer
   for y in range(1,StepsPerLayer):    #Each linear move in layer
      xpath.append(xpath[y+1])    #Put in the X coordinate from the yth step of layer 1
      ypath.append(ypath[y+1])    #Put in the Y coordinate from the yth step of layer 1
      zpath.append(x*LayerHeight) #Put in the Z coordinate of the next layer

      



if len(xpath) != len(ypath) or len(xpath) != len(zpath) or len(ypath) != len(zpath):
   print "Error-Pathlength Mismatch"
#print "x, y, and z path"
#print xpath
#print ypath
#print zpath

distance=0.0

for x in xrange(len(xpath)): # This initializes the arrays so I can 
    step.append(0.0)         #avoid that append() bullshit where I dont
    epath.append(0.0)        #know where I'm writing.

for x in xrange(3, len(xpath)): # This calculates how much extruder movement per step
    distance=((xpath[x]-xpath[x-1])**2+(ypath[x]-ypath[x-1])**2)**0.5
    step[x]=distance*GooCoefficient
    epath[x]=epath[x-1]+step[x]

#step[1]=((xpath[1]-xpath[0])*2+(ypath[1]-ypath[0])**2)


#print xpath
#print ypath
#print zpath
#print epath
#print step
#print "*********************************************************************************************"

#for x in range(len(xpath)): #Human readable raw output
#   print xpath[x-1], ypath[x-1], zpath[x-1], step[x-1], epath[x-1]

print "///////////////////////////////////////////////////////////////////////////////////////////"
for x in range(len(xpath)): #Gcode movements
   print "G1 X",xpath[x-1]," Y",ypath[x-1]," Z",zpath[x-1]," E",epath[x-1], "F360" #feedrate is guess for now
   







