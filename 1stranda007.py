import Shapes
print "Gcode generator Alpha 0.0004"
xpath = []  #These are initialized and default values
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


#config = open("config.txt", "wb")#This writes printer settings to config.txt
#config.write( "LayerHeight =\n");
#config.write(str(LayerHeight));
#config.write("\n");
#config.write( "ExtrusionWidth =\n");
#config.write(str(ExtrusionWidth));
#config.write("\n");
#config.write( "FilamentDiameter =\n");
#config.write(str(FilamentDiameter));
#config.write("\n");
#config.write( "FilamentDiameter =\n");
#config.write(str(FilamentDiameter));
#config.write("\n");
#config.write( "GooCoefficient =\n");
#config.write(str(GooCoefficient));
#config.write("\n");
#config.close()


print "GooCoefficient is the amount of millimeters of filament that will be pushed per millimeter of xy travel"
print "The GooCoefficient is calculated based on parameters LayerHeight, ExtrusionWidth, and FilamentDiameter"
print "Current values are:"
print "LayerHeight =", LayerHeight
print "ExtrusionWidth=", ExtrusionWidth
print "FilamentDiameter=", FilamentDiameter
print "GooCoefficient=", GooCoefficient


Default = raw_input("[Y] to keep settings, [N] to change them, [L] to load from config.txt")
if Default=='y' or Default == 'Y':
   print "wiggity-waaaaa"
if Default=='n' or Default=='N':
   LayerHeight=float(raw_input("LayerHeight:"))
   ExtrusionWidth=float(raw_input("ExtrusionWidth:"))
   FilamentDiameter=float(raw_input("FilamentDiameter:"))
   GooCoefficient = LayerHeight * ExtrusionWidth / FilamentArea
   print "GooCoefficient is calculated to", GooCoefficient
   GooCoefficient=float(raw_input("Override GooCoefficient or 0 to use calculated value"))
   if GooCoefficient==0:
      GooCoefficient = LayerHeight * ExtrusionWidth / FilamentArea
      print "Goo Coefficient Calculated to", GooCoefficient
   save1=raw_input("[Y] to save settings, [N] to not save them")
   if save1=='y' or save1=='Y':
      config = open("config.txt", "wb")#This writes printer settings to config.txt
      config.write( "LayerHeight =\n");#The order here must match the order in the load coad
      config.write(str(LayerHeight));
      config.write("\n");
      config.write( "ExtrusionWidth =\n");
      config.write(str(ExtrusionWidth));
      config.write("\n");
      config.write( "FilamentDiameter =\n");
      config.write(str(FilamentDiameter));
      config.write("\n");
      config.write( "FilamentDiameter =\n");
      config.write(str(FilamentDiameter));
      config.write("\n");
      config.write( "GooCoefficient =\n");
      config.write(str(GooCoefficient));
      config.write("\n");
      config.close()
if Default=='l' or Default == 'L':
   config = open("config.txt", "r") #This reads printer settings from config.txt
   garbage = config.readline()      #The order here must match the order in the save code.  
   LayerHeight=float(config.readline())
   garbage = config.readline()
   ExtrusionWidth=float(config.readline())
   garbage = config.readline()
   FilamentDiameter=float(config.readline())
   garbage = config.readline()
   GooCoefficient=float(config.readline())
   config.close()
   print "Current values are:"
   print "LayerHeight =", LayerHeight
   print "ExtrusionWidth=", ExtrusionWidth
   print "FilamentDiameter=", FilamentDiameter
   print "GooCoefficient=", GooCoefficient
   
   
      
      

#The rectangle code is in Shapes.py.  I'm trying to build a library there.

shapechoice = raw_input("[C]ircle or [R]ectangle")
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


print "//////////////////////////////////////////"
print "//////////////////////////////////////////"
print "G28"
for x in range(len(xpath)): #Gcode movements visible text output
   print "G1 X",xpath[x]," Y",ypath[x]," Z",zpath[x]," E",epath[x], "F480" #feedrate is guess for now


goutput = open("output1.gcode", "wb") #Now save to output1.gcode
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
   goutput.write( " F480 \n" );
goutput.close()






