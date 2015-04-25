

 1strand
An open source g-code generator for 3d printers that makes parts from a single continuous extrudate.

Major known problems:
Circles and rectangles follow the path of their alleged outer coordinates, so everything is big by half an extrusion width
Feedrate is set to 480 hardcoded.  My printer seems to move much slower than 480mm/s, but much faster than 480mm/min 
My printer also makes angry noises at the start of the print, probably from the plain Z move 
Program crashes when input is unexpectedly not floating point number
No extrusion "priming", skirt or brim functions.



a002 hardcoded parameters for a 1cm square/cube

a003 User-entered parameters for an arbitrary rectangle and printer.

a004 Actually tested to produce a physical rectangle.  Corrected G-code syntax in final line

a005 Added circle and tested to create physical circle.  Added untested prompt/choice for the shape.  Moved rectangle function and circle to shapes.py

a006 Added save / load settings to config.txt

a007 Added output to output1.gcode.  Overwrites without prompting.

a008 Added and tested keyboard input coordinates.  Created save and function for any shape.

a009 User interface has a main program loop, and abstracts printer option handling to printconfig.py

Immediate Goals:
Perimeter following coordinates from spreadsheet
Create objects with paths that end somewhere other than they start, but reverse the process each layer so the strand isn't broken
Perfect Bushing Tool
Clone copies of objects to print sequentially.  Parallel would require extruder stoppage, which kind of defeats the point.
Fillet radii

Long Term Goals:
All kinds of printer hardware optimization/kludges
Object creation interface
CAD file input
Non-planar prints
