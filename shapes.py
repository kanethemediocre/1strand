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
       
   xxpath.append(0.0) #first point at origin
   yypath.append(0.0)
   zzpath.append(0.0)

   xxpath.append(0)  #Then lift Z
   yypath.append(0)
   zzpath.append(zstart)  

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

   xxpath.append(0)
   yypath.append(0)
   zzpath.append(0)

   xxpath.append(0)
   yypath.append(0)
   zzpath.append(layer1)

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

                  
   
   
