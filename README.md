

 1strand
An open source g-code generator for 3d printers that makes parts from a single continuous extrudate.

Still puts the last instruction at the start.

a002 hardcoded parameters for a 1cm square/cube

a003 User-entered parameters for an arbitrary rectangle and printer.

a004 Actually tested to produce a physical rectangle.  Corrected G-code syntax in final line

a005 Added circle and tested to create physical circle.  Added untested prompt/choice for the shape.  Moved rectangle function and circle to shapes.py

a006 Added save / load settings to config.txt

a007 Added output to output1.gcode.  Overwrites without prompting.

a008 Added and tested keyboard input coordinates.  Created save function for any shape, but no load functionality yet.

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
