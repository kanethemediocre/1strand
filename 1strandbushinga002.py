#1strand Bushing Tool
#Standalone program for minimized cruft
import math

print "This program is for printing the best possible circular bushings"
print "Printer config values are hardcoded for ease of use (for me)"
xpath = []  #These are initialized and default values
ypath = []
zpath = []
step = []
epath = []
xstart = 10.0
ystart = 10.0
zstart = 0.5
height = 0.0
LayerHeight = 0.3
ExtrusionWidth = 0.6
FilamentDiameter=3
FilamentArea = FilamentDiameter * FilamentDiameter * 3.14159 / 4.0
GooCoefficient = LayerHeight * ExtrusionWidth / FilamentArea
configlist = [LayerHeight, ExtrusionWidth, FilamentDiameter, GooCoefficient]

BrimDiameter = 0.0
OuterDiameter = 0.0
InnerDiameter = 0.0
N = 1
ActualExtrusionWidth = ExtrusionWidth

print "Current values are:"
print "LayerHeight =", configlist[0]  #This assignment is super important
print "ExtrusionWidth=", configlist[1] #and needs to be consistent with
print "FilamentDiameter=", configlist[2] #with other code blocks related
print "GooCoefficient=", configlist[3] #to these options.
BrimDiameter = float(raw_input("Enter brim diameter in mm:"))
OuterDiameter = float(raw_input("Enter Outer Diameter in mm:"))
InnerDiameter = float(raw_input("Enter Inner Diameter in mm:"))
N = int(raw_input("Enter number of line segments in your alleged circles"))
anglestep = 2 * math.pi / N
print "Angular step is ", anglestep, " radians."
height = float(raw_input("Enter Height"))
centerx = (BrimDiameter / 2.0)+5 #Center is chosen so brim is 5mm from edge
centery = (BrimDiameter / 2.0)+5 #Center is chosen so brim is 5mm from edge

thickness = (OuterDiameter-InnerDiameter)/2
perimeters = thickness/ExtrusionWidth
print "Thickness = ", thickness
print "Needed perimeters = ", perimeters
perimeters = int(perimeters)
ActualExtrusionWidth = thickness/perimeters
print "Revised perimeters = ", perimeters
print "Revised extrusion width = ", ActualExtrusionWidth

BrimThickness = (BrimDiameter-InnerDiameter)/2
BrimPerimeters = int(BrimThickness/ActualExtrusionWidth)
print "Brim Thickness = ", BrimThickness
print "Brim Perimeters = ", BrimPerimeters

#Brim layer is first, and treated separately.

j=0
i=0
radius = BrimDiameter/2 - (j+0.5)*ActualExtrusionWidth
xpath.append(centerx+radius)
ypath.append(centery)
zpath.append(LayerHeight)
while (j<BrimPerimeters):
    radius = BrimDiameter/2 - (j+0.5)*ActualExtrusionWidth
    j=j+1
    i=0
    while (i<N):
        i=i+1
        #print "i=", i, "j=", j, "radius=", radius
        xpath.append(centerx+radius*math.cos(i*anglestep))
        ypath.append(centery+radius*math.sin(i*anglestep))
        zpath.append(LayerHeight)
#
#
#
#Now the actual bushing begins printing.
#
#
#
CurrentLayer=1
CurrentHeight=LayerHeight*CurrentLayer  #Technically should be earlier but wutev 
#
#
#
#Now the actual bushing begins printing.
#
#
#

#k=0

##Even layers (1st bushing layer is 2) are inside to outside
##odd layers are outside to inside, to maintain strand continuity
#j=0
#i=0
#radius = InnerDiameter/2 + (j-0.5)*ActualExtrusionWidth
#xpath.append(centerx+radius)
#ypath.append(centery)
#zpath.append(CurrentHeight)
#while (j<=perimeters):
#    radius = InnerDiameter/2 + (j-0.5)*ActualExtrusionWidth
#    j=j+1
#    i=0
#    while (i<N):
#        i=i+1
#        #print "i=", i, "j=", j, "radius=", radius
#        xpath.append(centerx+radius*math.cos(i*anglestep))
#        ypath.append(centery+radius*math.sin(i*anglestep))
#        zpath.append(CurrentHeight)
##odd layers are outside to inside, to maintain strand continuity
#CurrentLayer=3
#CurrentHeight=LayerHeight*CurrentLayer   
#j=0
#i=0
#radius = OuterDiameter/2 - (j+0.5)*ActualExtrusionWidth
#xpath.append(centerx+radius)
#ypath.append(centery)
#zpath.append(CurrentHeight)
#while (j<perimeters):
#    radius = OuterDiameter/2 - (j+0.5)*ActualExtrusionWidth
#    j=j+1
#    i=0
#    while (i<N):
#        i=i+1
#        #print "i=", i, "j=", j, "radius=", radius
#        xpath.append(centerx+radius*math.cos(i*anglestep))
#        ypath.append(centery+radius*math.sin(i*anglestep))
#        zpath.append(CurrentHeight)

while (CurrentLayer*LayerHeight < height):
    CurrentLayer=CurrentLayer+1
    CurrentHeight=LayerHeight*CurrentLayer 
    #Even layers (1st bushing layer is 2) are inside to outside
    #odd layers are outside to inside, to maintain strand continuity
    j=1
    i=0
    radius = InnerDiameter/2 + (j-0.5)*ActualExtrusionWidth
    xpath.append(centerx+radius)
    ypath.append(centery)
    zpath.append(CurrentHeight-LayerHeight*0.75)
    while (j<=perimeters):
        radius = InnerDiameter/2 + (j-0.5)*ActualExtrusionWidth
        j=j+1
        i=0
        while (i<(N-1)): #kludge
            i=i+1
            #print "i=", i, "j=", j, "layer=", CurrentLayer, "radius=", radius
            xpath.append(centerx+radius*math.cos(i*anglestep))
            ypath.append(centery+radius*math.sin(i*anglestep))
            if (i==1 and j==1):
                zpath.append(CurrentHeight-LayerHeight*.25)
            else:
                zpath.append(CurrentHeight)
    #odd layers are outside to inside, to maintain strand continuity
    CurrentLayer=CurrentLayer+1
    CurrentHeight=LayerHeight*CurrentLayer   
    j=0
    i=0
    radius = OuterDiameter/2 - (j+0.5)*ActualExtrusionWidth
    xpath.append(centerx+radius)
    ypath.append(centery)
    zpath.append(CurrentHeight-LayerHeight*.75)
    while (j<perimeters):
        radius = OuterDiameter/2 - (j+0.5)*ActualExtrusionWidth
        j=j+1
        i=0
        while (i<(N-1)): #Same kludge as the even layers.
            i=i+1
            #print "i=", i, "j=", j, "layer=", CurrentLayer, "radius=", radius
            xpath.append(centerx+radius*math.cos(i*anglestep))
            ypath.append(centery+radius*math.sin(i*anglestep))
            if (i==1 and j==1):
                zpath.append(CurrentHeight-LayerHeight*.25)
            else:
                zpath.append(CurrentHeight)
            





#Extrusion is only handled here temporarily for testing
for x in xrange(len(xpath)): # This initializes the arrays so I can 
    step.append(0.0)         #avoid that append() bullshit where I dont
    epath.append(0.0)        #know where I'm writing.

for x in xrange(2, len(xpath)): # This calculates how much extruder movement per step
    distance=((xpath[x]-xpath[x-1])**2+(ypath[x]-ypath[x-1])**2)**0.5
    step[x]=distance*GooCoefficient
    epath[x]=epath[x-1]+step[x]
#for x in range(len(xpath)): #Human readable raw output
#   print xpath[x-1], ypath[x-1], zpath[x-1], step[x-1], epath[x-1]

goutput = open("output1.gcode", "wb") #Now save to output1.gcode
goutput.write("G28 \nG21 \nG90 \nG92 E0 \nM82")
x=0
for x in range(len(xpath)):
   goutput.write("G1 X"  );
   goutput.write( str(xpath[x]) );
   goutput.write( " Y" );
   goutput.write( str(ypath[x]) );
   goutput.write( " Z" );
   goutput.write( str(zpath[x]) );
   goutput.write( " E" );
   goutput.write( str(epath[x]) );
   goutput.write( " F2000 \n" );
goutput.close()

