import Shapes #Stores and changes path information
import printconfig #Stores and changes printer hardware related settings


print "Gcode generator Alpha 0.0009"
xpath = []  #These are initialized and default values
ypath = []
zpath = []
step = []
epath = []
xstart = 10.0
ystart = 10.0
zstart = 0.5
height = 0.0
LayerHeight = 0.5
ExtrusionWidth = 1.0
FilamentDiameter=1.75
FilamentArea = FilamentDiameter * 3.14159 / 4.0
GooCoefficient = LayerHeight * ExtrusionWidth / FilamentArea
configlist = [LayerHeight, ExtrusionWidth, FilamentDiameter, GooCoefficient]

#print "GooCoefficient is the amount of millimeters of filament that will be pushed per millimeter of xy travel"
#print "The GooCoefficient is calculated based on parameters LayerHeight, ExtrusionWidth, and FilamentDiameter"
#print "Current printer values are:"
#print "LayerHeight =", LayerHeight
#print "ExtrusionWidth=", ExtrusionWidth
#print "FilamentDiameter=", FilamentDiameter
#print "GooCoefficient=", GooCoefficient
#printconfig.reconfigprinter(LayerHeight, ExtrusionWidth, FilamentDiameter, GooCoefficient)


   
   
      
#These movements are the beginning for ANY print      

xpath.append(0)  #Lift Z (homing takes to 0,0)
ypath.append(0)
zpath.append(LayerHeight) #This is not the 1st layer height.  That is input later

#Main program loop starts here

shapechoice = '0'
while shapechoice != 'E' and shapechoice != 'e':
   print "Current printer values are:"
   print "LayerHeight =", configlist[0]  #This assignment is super important
   print "ExtrusionWidth=", configlist[1] #and needs to be consistent with
   print "FilamentDiameter=", configlist[2] #with other code blocks related
   print "GooCoefficient=", configlist[3] #to these options.
   if len(xpath) > 3: 
      print "Shape is loaded with", len(xpath), "steps." #3 is minimum steps because 2 are added as initialization.
      print "Height is ", height
   else:
      print "No shape loaded."
   shapechoice = raw_input("[C]ircle, [R]ectangle, [I]nput Path, [L]oad shape, [S]ave shape, [E]xport gcode, [O]ptions, or [Q]uit")

   if shapechoice == 'R' or shapechoice == 'r':
      height=Shapes.rectanglecreator(xpath,ypath,zpath)
   if shapechoice == 'C' or shapechoice == 'c':
      height = Shapes.circlecreator(xpath,ypath,zpath)
   if shapechoice == 'I' or shapechoice == 'i':
      height = Shapes.inputpath(xpath, ypath, zpath)
   if shapechoice == 'L' or shapechoice == 'l':
      loadedfilename = Shapes.loadfile(xpath, ypath, zpath)
   if shapechoice == 'S' or shapechoice == 's':
      savedfilename = Shapes.savefile(xpath, ypath, zpath)
   if shapechoice == 'O' or shapechoice == 'o':
      printconfig.reconfigprinter(configlist)
   if shapechoice == 'E' or shapechoice == 'e':
      quitflag = 2
      print "export as function not implemented yet, exporting and quitting..."

#above comments make


#This assumes the layer paths end where they start.
#Finding the number of steps in a layer (at this point, just 1 perimeter of a layer)
#is important for all sorts of post-processing to that shape.
StepsPerLayer=len(xpath)-1 #need to update this value to accomodate multiple perimeters
#Try assumption that inside is always the +x, Xy direction.
   


#Below is a layer multiplying function that assumes the start
#and end are in the same place
for x in range(2, int(height/LayerHeight)+1): #Each layer
   for y in range(1,StepsPerLayer):    #Each linear move in layer
      xpath.append(xpath[y+1])    #Put in the X coordinate from the yth step of layer 1
      ypath.append(ypath[y+1])    #Put in the Y coordinate from the yth step of layer 1
      zpath.append(x*LayerHeight) #Put in the Z coordinate of the next layer

 
if len(xpath) != len(ypath) or len(xpath) != len(zpath) or len(ypath) != len(zpath):
   print "Error-Pathlength Mismatch"

distance=0.0

for x in xrange(len(xpath)): # This initializes the arrays so I can 
    step.append(0.0)         #avoid that append() bullshit where I dont
    epath.append(0.0)        #know where I'm writing.

for x in xrange(3, len(xpath)): # This calculates how much extruder movement per step
    distance=((xpath[x]-xpath[x-1])**2+(ypath[x]-ypath[x-1])**2)**0.5
    step[x]=distance*GooCoefficient
    epath[x]=epath[x-1]+step[x]

#step[1]=((xpath[1]-xpath[0])*2+(ypath[1]-ypath[0])**2)


#print "//////////////////////////////////////////"
#print "//////////////////////////////////////////"
#print "G28"
#for x in range(len(xpath)): #Gcode movements visible text output
#   print "G1 X",xpath[x]," Y",ypath[x]," Z",zpath[x]," E",epath[x], "F480" #feedrate is guess for now


goutput = open("output1.gcode", "wb") #Now save to output1.gcode
goutput.write("G28 \n")
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






