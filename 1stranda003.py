print "Gcode generator Alpha 0.0002"
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
FilamentArea = FilamentDiameter * 3.14159 / 4.0
GooCoefficient = LayerHeight * ExtrusionWidth / FilamentArea
print "GooCoefficient is the amount of millimeters of filament that will be pushed per millimeter of xy travel"
print "The GooCoefficient is calculated based on parameters LayerHeight, ExtrusionWidth, and FilamentDiameter"
print "Default values are:"
print "LayerHeight =", LayerHeight
print "ExtrusionWidth=", ExtrusionWidth
print "FilamentDiameter=", FilamentDiameter
print "GooCoefficient=", GooCoefficient
#print GooCoefficient
#print "the amount of millimeters of filament that will be pushed per"
#print "millimiter of xy travel"


Default = raw_input("Do you [Y]earn for the default settings or want to [N]itpick?")

if Default=='y' or Default == 'Y':
   print "wiggity-waaaaa"
if Default=='n' or Default=='N':
   LayerHeight=float(raw_input("LayerHeight:"))
   ExtrusionWidth=float(raw_input("ExtrusionWidth:"))
   FilamentDiameter=float(raw_input("FilamentDiameter:"))#   print 'You fail at input.'
   GooCoefficient=float(raw_input("Override GooCoefficient or 0 to calculate:"))
if GooCoefficient==0:
   GooCoefficient = LayerHeight * ExtrusionWidth / FilamentArea
   print "Goo Coefficient Calculated to", GooCoefficient

print "Rectangles are all I got right now. 1 perimeter."
xsize = float(raw_input("Enter X Size:"))
ysize = float(raw_input("Enter Y Size:"))
zsize = float(raw_input("Enter Z Size:"))
Perimeters = 1

xstart = float(raw_input("Enter X Start:"))
ystart = float(raw_input("Enter Y Start:"))
zstart = float(raw_input("Enter Z Start:"))
    
xpath.append(0.0) #first point at origin
ypath.append(0.0)
zpath.append(0.0)

xpath.append(0)  #Then lift Z
ypath.append(0)
zpath.append(zstart)  

xpath.append(xstart)  #Then move to start position
ypath.append(ystart)
zpath.append(zstart)
#
#From here on is code specific to the test print I'm attempting.  A square atm
#
print "Rectangles are all I got right now. 1 perimeter."
xsize = float(raw_input("Enter X Size:"))
ysize = float(raw_input("Enter Y Size:"))
zsize = float(raw_input("Enter Z Size:"))
Perimeters = 1

xpath.append(xstart+xsize)
ypath.append(ystart)
zpath.append(zstart)

xpath.append(xstart+xsize)
ypath.append(ystart+ysize)
zpath.append(zstart)

xpath.append(xstart)
ypath.append(ystart+ysize)
zpath.append(zstart)

xpath.append(xstart)
ypath.append(ystart)
zpath.append(zstart)
#This is a single-layer square. Next I'll try to copypasta to add height
#This assumes the layer paths end where they start.
StepsPerLayer=len(xpath)-1
for x in range(2, int(zsize/LayerHeight)+1): #Each layer
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
print "*********************************************************************************************"

for x in range(len(xpath)): #Human readable raw output
   print xpath[x-1], ypath[x-1], zpath[x-1], step[x-1], epath[x-1]

print "///////////////////////////////////////////////////////////////////////////////////////////"
for x in range(len(xpath)): #Gcode movements
   print "G01 x",xpath[x-1]," y",ypath[x-1]," z",zpath[x-1]," e",epath[x-1], "f100" #feedrate is guess for now
   






