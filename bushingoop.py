import math


class PrinterProperties(object):
    def __init__(self, filament_diameter=3.0, nozzle_diameter=1.0):
        self.filament_diameter = filament_diameter
        self.nozzle_diameter = nozzle_diameter


class PrintSettings(object):
    def __init__(self, layer_height=1.0, edge_distance=8.0,
                 brim_diameter=40.0, circle_resolution=24, feed_rate=2000.0,
                 extrusion_multiplier=1.0):
        self.layer_height = layer_height
        self.feed_rate = feed_rate
        self.edge_distance = edge_distance
        self.brim_diameter = brim_diameter
        self.circle_resolution = circle_resolution
        self.extrusion_multiplier = extrusion_multiplier
        self.x_center = brim_diameter / 2 + edge_distance
        self.y_center = brim_diameter / 2 + edge_distance


class LayerProperties(object):
    def __init__(self, inner_radius=6.0, outer_radius=10.0, height=0, extruder_position=0, direction=1):
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.height = height
        self.extruder_position = extruder_position
        self.direction = direction

    def perimeter_quantity(self, nozzle_diameter):
        return self.radial_difference() / nozzle_diameter

    def radial_difference(self):
        return (self.outer_radius - self.inner_radius) / 2

    def extrusion_width(self, nozzle_diameter):
        perimeters = self.perimeter_quantity(nozzle_diameter)
        return nozzle_diameter + (self.radial_difference() - perimeters * nozzle_diameter) / perimeters


class DiscLayer(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates


class Coordinate(object):
    def __init__(self, x, y, z, extruder_position, feed_rate):
        self.x = x
        self.y = y
        self.z = z
        self.extruder_position = extruder_position
        self.feed_rate = feed_rate


class DiscLayerFactory(object):
    def __init__(self, printer_properties):
        self.printer_properties = printer_properties

    def make(self, layer_properties, print_settings):
        coordinates = []

        extrusion_width = layer_properties.extrusion_width(print_settings.nozzle_diameter)

        if layer_properties.direction == 1:
            first_x = print_settings.x_center - layer_properties.outer_radius + extrusion_width / 2
            radius = layer_properties.outer_radius - extrusion_width / 2  # Radius is active radius
        else:
            first_x = print_settings.x_center - layer_properties.inner_radius - extrusion_width/ 2
            radius = layer_properties.inner_radius - extrusion_width / 2  # Starts at inner or outer based on D(irection)

        first_coordinate = Coordinate(first_x, layer_properties.y_center, layer_properties.height,
                                  layer_properties.extruder_position, print_settings.feed_rate)

        coordinates = [first_coordinate]

        previous_coordinate = first_coordinate

        extrusion_ratio = self.extrusion_ratio(extrusion_width, print_settings)

        while ((radius > layer_properties.inner_radius + extrusion_width) and (layer_properties.direction == 1)) or \
            ((radius < layer_properties.outer_radius - extrusion_width) and (layer_properties.direction == -1)):
            coordinates.extend(self.make_perimeter(previous_coordinate, extrusion_ratio, layer_properties,
                                                   print_settings, radius, lambda i,z,t,l: z))
            previous_coordinate = coordinates[-1]
            radius = radius - extrusion_width * layer_properties.direction

        coordinates.extend(self.make_perimeter(coordinates[-1], extrusion_ratio, layer_properties,
                                              print_settings, radius, self.final_perimeter_z))

        layer = DiscLayer(coordinates)
        return layer

    def make_perimeter(self, previous_coordinate, extrusion_ratio, layer_properties, print_settings, radius, z_calculator):
        coordinates = []

        for i in range(0, print_settings.circular_resolution):
            new_coordinate = self.make_coordinate(i, print_settings.x_center, print_settings.y_center, layer_properties.height, radius,
                                 print_settings.circular_resolution, previous_coordinate, extrusion_ratio,
                                 print_settings.feed_rate, print_settings.layer_height)
            previous_coordinate = new_coordinate
            coordinates.append(new_coordinate)
        return coordinates

    def final_perimeter_z(self, idx, height, theta, layer_height):
        return height + (1 - math.cos((theta - math.pi) / 2)) * layer_height * .5

    def make_coordinate(self, index, x_center, y_center, height, radius, resolution, previous_coordinate, extrusion_ratio, feed_rate, layer_height, z_calculator):
        theta = math.pi + index * (2 * math.pi / resolution)
        x_location = math.cos(theta) * radius + x_center
        y_location = math.sin(theta) * radius + y_center
        z_location = z_calculator(index, height, theta, layer_height)

        distance = ((x_location - previous_coordinate.x) ** 2 + (y_location - previous_coordinate.y) ** 2) ** 0.5
        e_location = previous_coordinate.extruder_position + distance + extrusion_ratio
        return Coordinate(x_location, y_location, z_location, e_location, feed_rate)

    def extrusion_ratio(self, extrusion_width, print_settings):
        return print_settings.extrusion_multiplier * print_settings.layer_height * extrusion_width / \
               (print_settings.filament_diameter ** 2 * math.pi / 4.0)




def DiscBlended(x, y, z, R, r, n, s, ND, FD, GM, LH, D, Epos):
    Perimeters = int(((R - r) / 2) / ND)
    ExtrusionWidth = ND + (((R - r) / 2) - Perimeters * ND) / Perimeters
    ExtrusionRatio = GM * LH * ExtrusionWidth / (FD * FD * 3.14156 / 4.0)
    if D == 1:
        xx = [x - R + ExtrusionWidth / 2]
        Radius = R - ExtrusionWidth / 2  # Radius is active radius
    else:
        xx = [x - r - ExtrusionWidth / 2]
        Radius = r - ExtrusionWidth / 2  # Starts at inner or outer based on D(irection)
    yy = [y]
    zz = [z]
    ee = [Epos]
    ff = [s]
    while ((Radius > r + ExtrusionWidth) and (D == 1)) or ((Radius < R - ExtrusionWidth) and (D == -1)):

        i = 1
        while (i <= n):
            Theta = math.pi + i * (2 * math.pi / n)
            xx.append(math.cos(Theta) * Radius + x)
            yy.append(math.sin(Theta) * Radius + y)
            zz.append(z)
            # zz.append( z+(1-math.cos((Theta-math.pi)/2))*LH*.5 )
            Distance = ((xx[len(xx) - 1] - xx[len(xx) - 2]) ** 2 + (yy[len(yy) - 1] - yy[len(yy) - 2]) ** 2) ** 0.5
            ee.append(ee[len(ee) - 1] + Distance * ExtrusionRatio)
            ff.append(s)
            i = i + 1
        Radius = Radius - ExtrusionWidth * D
    while ((Radius > r) and (D == 1)) or ((Radius < R) and (D == -1)):  # 1 loop for now
        i = 1
        while (i <= n):
            Theta = math.pi + i * (2 * math.pi / n)
            xx.append(math.cos(Theta) * Radius + x)
            yy.append(math.sin(Theta) * Radius + y)
            # zz.append(z)
            zz.append(z + (1 - math.cos((Theta - math.pi) / 2)) * LH * .5)
            Distance = ((xx[len(xx) - 1] - xx[len(xx) - 2]) ** 2 + (yy[len(yy) - 1] - yy[len(yy) - 2]) ** 2) ** 0.5
            ee.append(ee[len(ee) - 1] + Distance * ExtrusionRatio)
            ff.append(s)
            i = i + 1
        Radius = Radius - ExtrusionWidth * D

    return xx, yy, zz, ee, ff


TB = DiscBlended(XCenter, YCenter, Height, OD / 2, ID / 2, CircleN, Speed, NozzleDiameter, FilamentDiameter,
                 GooMultiplier, LayerHeight, 1, Eposition)
# print TB
TB2 = DiscBlended(XCenter, YCenter, Height + LayerHeight, OD / 2, ID / 2, CircleN, Speed, NozzleDiameter,
                  FilamentDiameter, GooMultiplier, LayerHeight, -1, Eposition)
TB[0].extend(TB2[0])
TB[1].extend(TB2[1])
TB[2].extend(TB2[2])
TB[3].extend(TB2[3])
TB[4].extend(TB2[4])
# print TB[2]

















goutput = open("output1.gcode", "wb")  # Now save to output1.gcode
goutput.write("G28 \nG21 \nG90 \nG92 E0 \nM82")
x = 0
for x in range(len(TB[0])):
    goutput.write("G1 X");
    goutput.write(str(TB[0][x]));
    goutput.write(" Y");
    goutput.write(str(TB[1][x]));
    goutput.write(" Z");
    goutput.write(str(TB[2][x]));
    goutput.write(" E");
    goutput.write(str(TB[3][x]));
    goutput.write(" F");
    goutput.write(str(TB[4][x]));
    goutput.write(" \n");
# goutput.write( "G1 Z" );
# goutput.write( str(height+10) );
# goutput.write( " F400 \n" );
goutput.close()

xpos = 1  # mm First point is established in these declarations.
ypos = 1  # mm
zpos = 5  # mm No need to drag 0,0 poop along the bed into the print
epos = 0  # mm
step = 0  # mm
feed = 1000  # mm per minute




