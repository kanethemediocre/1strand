#This contains functions relating to the changing, saving, displaying of the printer settings.
#Stuff like layer height, goo coefficient, 1st layer height
import math

def reconfigprinter(cconfiglist):
   Default = raw_input("[Y] to keep settings, [N] to change them, [L] to load from config.txt")
   if Default=='y' or Default == 'Y':
      print "wiggity-waaaaa"
   if Default=='n' or Default=='N':
      cconfiglist[0]=float(raw_input("LayerHeight:"))
      cconfiglist[1]=float(raw_input("ExtrusionWidth:"))
      cconfiglist[2]=float(raw_input("FilamentDiameter:"))
      FilamentArea = cconfiglist[2] * cconfiglist[2] * 3.14159/4.0
      cconfiglist[3] = cconfiglist[0] * cconfiglist[1] / FilamentArea
      print "GooCoefficient is calculated to", cconfiglist[3]
      cconfiglist[3]=float(raw_input("Override GooCoefficient or 0 to use calculated value"))
      if cconfiglist[3]==0:
         cconfiglist[3] = cconfiglist[0] * cconfiglist[1] / FilamentArea
         print "Goo Coefficient Calculated to", cconfiglist[3]
   save1 = 'n'
   if Default == 'n' or Default == 'N':
      save1=raw_input("[Y] to save settings, [N] to not save them")
   if save1=='y' or save1=='Y':
      config = open("config.txt", "wb")#This writes printer settings to config.txt
      config.write( "LayerHeight =\n");#The order here must match the order in the load coad
      config.write(str(cconfiglist[0]));
      config.write("\n");
      config.write( "ExtrusionWidth =\n");
      config.write(str(cconfiglist[1]));
      config.write("\n");
      config.write( "FilamentDiameter =\n");
      config.write(str(cconfiglist[2]));
      config.write("\n");
      config.write( "GooCoefficient =\n");
      config.write(str(cconfiglist[3]));
      config.write("\n");
      config.close()
   if Default=='l' or Default == 'L':
      config = open("config.txt", "r") #This reads printer settings from config.txt
      garbage = config.readline()      #The order here must match the order in the save code.  
      cconfiglist[0]=float(config.readline())
      garbage = config.readline()
      cconfiglist[1]=float(config.readline())
      garbage = config.readline()
      cconfiglist[2]=float(config.readline())
      garbage = config.readline()
      cconfiglist[3]=float(config.readline())
      config.close()
#   print "Current values are:"
#   print "LayerHeight =", LayerHeight
#   print "ExtrusionWidth=", ExtrusionWidth
#   print "FilamentDiameter=", FilamentDiameter
#   print "GooCoefficient=", GooCoefficient
   return;
