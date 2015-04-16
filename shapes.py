import math

def rectanglecreator(xxpath, yypath, zzpath):
   print "Rectangles are all I got right now. 1 perimeter."
   xsize = float(raw_input("Enter X Size:"))
   ysize = float(raw_input("Enter Y Size:"))
   zsize = float(raw_input("Enter Z Size:"))
   Perimeters = 1

   xstart = float(raw_input("Enter X Start:"))
   ystart = float(raw_input("Enter Y Start:"))
   zstart = float(raw_input("Enter Z Start:"))
       
   #xxpath.append(0.0) #first point at origin
   #yypath.append(0.0)
   #zzpath.append(0.0)

   #xxpath.append(0)  #Then lift Z
   #yypath.append(0)
   #zzpath.append(zstart)  

   xxpath.append(xstart)  #Then move to start position
   yypath.append(ystart)
   zzpath.append(zstart)

   #Assigns to a rectangle as defined above

   xxpath.append(xstart+xsize)
   yypath.append(ystart)
   zzpath.append(zstart)

   xxpath.append(xstart+xsize)
   yypath.append(ystart+ysize)
   zzpath.append(zstart)

   xxpath.append(xstart)
   yypath.append(ystart+ysize)
   zzpath.append(zstart)

   xxpath.append(xstart)
   yypath.append(ystart)
   zzpath.append(zstart)
   return zsize;

def circlecreator(xxpath, yypath, zzpath):
   radius = float(raw_input("Radius"))
   centerx = float(raw_input("X Center Coordinate (NOT 0 FOR MOST PRINTERS)"))
   centery = float(raw_input("Y Center Coordinate (NOT 0 FOR MOST PRINTERS)"))
   layer1 = float(raw_input("First Layer Height"))
   height = float(raw_input("Height"))
   N = int(raw_input("Resolution (steps / revolution)"))
   ewidth = float(raw_input("Extrusion width"))
   anglestep = 2 * math.pi / N

   #xxpath.append(0)
   #yypath.append(0)
   #zzpath.append(0)

   #xxpath.append(0)
   #yypath.append(0)
   #zzpath.append(layer1)

   xxpath.append(centerx+radius)
   yypath.append(centery)
   zzpath.append(layer1)
   i=0
   while(i < N):
      i=i+1
      xxpath.append(centerx+radius*math.cos(i*anglestep))
      yypath.append(centery+radius*math.sin(i*anglestep))
      zzpath.append(layer1)
   return height

def inputpath(xxpath, yypath, zzpath):
   print "This function can create a custom 2d path input coordinates."
   inputpathfork = raw_input( "[L]oad file, or [K]eyboard input?")
   if inputpathfork == "K" or inputpathfork == "k":
      z1 = float(raw_input("1st layer height")) #Provisions should be made for this to be easily changed
      #xxpath.append(0.0)
      #yypath.append(0.0)
      #zzpath.append(0.0)
      
      #xxpath.append(0.0)
      #yypath.append(0.0)
      #zzpath.append(z1)                       

      print "9999 to stop input"
      print "Current version expects last coordinate to match first."
      quitflag = 0
      while quitflag == 0:
         xxinput = float(raw_input("x"))
         if xxinput == 9999:
            quitflag = 1
         else:
            xxpath.append(xxinput)
         yyinput = float(raw_input("y"))
         if yyinput == 9999 or xxinput == 9999:
            quitflag = 1
         else:
            yypath.append(yyinput)
            zzpath.append(z1)
      
   return float(raw_input("Height?"))
      
         
def loadfile(xxpath, yypath, zzpath):
   print "This function can load a previously saved 2d shape"
   filename1 = open(raw_input("Filename?"), "r")
   Height = float(raw_input("Height?"))
   quitflag = 0
   i=0
   garbagex1 = filename1.readline() #First two movements
   garbagey1 = filename1.readline() #are origin and lift
   garbagez1 = filename1.readline() #which are already added 
   garbagezzz = filename1.readline() #to the path in the main
   garbagex1 = filename1.readline() #program.  We need to discard
   garbagey1 = filename1.readline() #them or they will get duplicated
   garbagez1 = filename1.readline() #by the loading process
   garbagezzz = filename1.readline()
   while quitflag == 0:
      line1 = filename1.readline()
      i=i+1 #This is the line number on the file.
      if line1 == "":
         quitflag=1
         print "End of file reached"
         print "Read", str(i), "lines.\n"
      else:
         if ( i % 4 ) == 1:  #This where the file really gets parsed.           
            xxpath.append(float(line1)) #if i did this all in one
         if ( i % 4 ) == 2:             #loop execution i'd have
            yypath.append(float(line1)) #end of file being passed as 
         if ( i % 4 ) == 3:             #a float and shitting more bricks
            zzpath.append(float(line1)) #if it ends unexpectedly.
         if ( i % 4 ) == 0:
            if line1 != "zzz\n":
               print "file flag error at line", str(i)
   filename1.close()
   Height = float(raw_input("Height?"))
   return Height       
            
            
            
         
      
   
   
