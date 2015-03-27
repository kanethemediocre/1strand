# 1strand
An open source g-code generator for 3d printers that makes parts from a single continuous extrudate.

Still puts the last instruction at the start.

v002 hardcoded parameters for a 1cm square/cube
v003 User-entered parameters for an arbitrary rectangle and printer.

Goals:
Perimeter following coordinates from spreadsheet
Create objects with paths that end somewhere other than they start, but reverse the process each layer so the strand isn't broken
Clone copies of objects to print sequentially.  Parallel would require extruder stoppage, which kind of defeats the point.
Fillet radii
