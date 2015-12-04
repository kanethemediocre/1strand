import math

LayerHeight = 0.3 #mm
FilamentDiameter = 3.0 #mm
NozzleDiameter = 0.6 #mm
Speed = 2000 #mm per minute.
FirstLayerHeight = 0.3 #mm
InnerDiameter = 12.0 #mm
OuterDiameter = 20.0 #mm
BrimDiameter = 40.0 #mm
EdgeDistance = 8.0 #mm
CircleN = 24 #Raw integer.  Number of points in a circle.
GooMultiplier = 1.0 #yeah.
ClimbSteps = 4 #This will get interesting
#All above this is supposed to be user settings



xpos = 1 #mm First point is established in these declarations.
ypos = 1 #mm
zpos = 5 #mm No need to drag 0,0 poop along the bed into the print
epos = 0 #mm
step = 0 #mm
feed = 1000 #mm per minute

XCenter = BrimDiameter/2 + EdgeDistance #mm Unnecessary variables.
YCenter = BrimDiameter/2 + EdgeDistance #mm
AngularStep=2*3.1416/CircleN

Perimeters = int(((OuterDiameter - InnerDiameter)/2)/NozzleDiameter)
#BasicWidth = (OuterDiameter - InnerDiameter)/2
#WidthAsIs = Perimeters*NozzleDiameter
#Leftover = ((OuterDiameter - InnerDiameter)/2)-Perimeters*NozzleDiameter
ExtrusionWidth = NozzleDiameter + (((OuterDiameter - InnerDiameter)/2)-Perimeters*NozzleDiameter)/Perimeters
#GooArea = LayerHeight * ExtrusionWidth
#FilamentArea = FilamentDiameter*FilamentDiameter*3.14156/4.0
ExtrusionRatio = LayerHeight * ExtrusionWidth /(FilamentDiameter*FilamentDiameter*3.14156/4.0)
print Perimeters,  ExtrusionWidth, ExtrusionRatio
#Perimeters, ExtrusionWidth, and ExtrusionRatio are all we need from that pile.


def Circle1(x, y, z, r, n):
#XYZ are center coords, R and r are radii, E is the extrusion ratio, n is segments
    xx=[x-r]
    yy=[y]
    zz=[z]
    i=1
    while (i<n):
        Theta = math.pi + i*(2*math.pi/n)
        xx.append(math.cos(Theta)*r+x)
        yy.append(math.sin(Theta)*r+y)
        zz.append(z)
        i=i+1
    return [xx,yy,zz]
stuff = Circle1(XCenter, YCenter, LayerHeight, InnerDiameter, CircleN)
#print stuff

def Circle1Blend(x, y, z, r, n, h):
    xx=[x-r]
    yy=[y]
    zz=[z]
    i=1
    while (i<n):
        Theta = math.pi + i*(2*math.pi/n)
        xx.append(math.cos(Theta)*r+x)
        yy.append(math.sin(Theta)*r+y)
        zz.append(z+(1-math.cos((Theta-math.pi)/2))*h*.5)
        i=i+1
    return [xx,yy,zz]
testcircle1blend = Circle1Blend(XCenter, YCenter, LayerHeight, InnerDiameter, CircleN, LayerHeight)
#print testcircle1blend
    
def Circle1BrimBlend(x, y, z, r, n, h):
    xx=[x-r]
    yy=[y]
    zz=[z]
    i=1
    while (i<n):
        Theta = math.pi + i*(2*math.pi/n)
        xx.append(math.cos(Theta)*r+x)
        yy.append(math.sin(Theta)*r+y)
        zz.append(z)
        i=i+1
    return [xx,yy,zz]

def SpiralIn(x,y,z,R,r,N,n,w):
    Chunk1 = Circle1(x,y,z,(R-w/2),n)
    xxx=Chunk1[0]
    yyy=Chunk1[1]
    zzz=Chunk1[2]
    j=1
    while (j<N):
        CurrentChunk=Circle1(x,y,z,(R-w/2-w*j),n)
        xxx.extend(CurrentChunk[0])
        yyy.extend(CurrentChunk[1])
        zzz.extend(CurrentChunk[2])
        j=j+1
    return [xxx, yyy, zzz]

def AddChunks(Chunk1, Chunk2):
    CombinedChunk=Chunk1
    if len(Chunk1)!=len(Chunk2):
        print "mismatch error"
    else:
        i=0
        while i<len(Chunk2):
            CombinedChunk[i].extend(Chunk2[i])
            i=i+1
    return CombinedChunk

            
foo = SpiralIn(XCenter,YCenter,LayerHeight, OuterDiameter,InnerDiameter, Perimeters, CircleN, ExtrusionWidth)
def BrimLayer1(x,y,z,R,r,N,n,w):
    StartSpiral=SpiralIn(XCenter,YCenter,LayerHeight, BrimDiameter, InnerDiameter+2*ExtrusionWidth, Perimeters-1, CircleN, ExtrusionWidth)
    BrimRiseSpiral=Circle1Blend(XCenter,YCenter,LayerHeight, InnerDiameter, CircleN, LayerHeight)
    
    return AddChunks(StartSpiral,BrimRiseSpiral)
foo2=BrimLayer1(XCenter,YCenter,LayerHeight, OuterDiameter,InnerDiameter, Perimeters, CircleN, ExtrusionWidth)
doofus = [12,13,14]
doofus2 = [15,16, 17]
doofus.extend(doofus2)
print doofus

print foo2
#print foo
#for end
#PathLength = sum(step)
#
