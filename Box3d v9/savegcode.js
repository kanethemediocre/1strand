function savegcode(zheight,layerheight,xloop,yloop,GooCoefficient,feedrate){//These variable names are the same as the globals passed into the function, not ideal.
	xpath = [];
	ypath = [];
	zpath = [];
	epath = [];
	var z=0;
	while (z<zheight){//For all layers (z coords)
		z=z+parseFloat(layerheight);
		xpath.push(xloop[0]);//adds first point
		ypath.push(yloop[0]);
		zpath.push(z);
		var i=0
		while (i<xloop.length-1){ //For all points in loop
			i=i+1;
			xpath.push(xloop[i]); //add point from xloop to xpath
			ypath.push(yloop[i]);
			zpath.push(z); //add z coordinate to zpath
			}
		}
	var i=1;
	epath.push(0);//Origin has 0 extruder position
	epath.push(0); //First point in polygon has 0 extruder position
	while (i<xpath.length-1){	
		i=i+1;
		var dx = xpath[i]-xpath[i-1];
		var dy = ypath[i]-ypath[i-1];
		var distance = Math.sqrt(dx*dx+dy*dy);
		var estep = distance*GooCoefficient;
		epath.push(epath[i-1]+estep);
	}
	var gcode = "G28 \nG21 \nG90 \nG92 E0 \nM82";
	var i=0
	gcode = gcode + "G1 X"+xpath[0];
	gcode = gcode + " Y" + ypath[0];
	gcode = gcode + " Z" + zpath[0];
	gcode = gcode + " E" + epath[0];
	gcode = gcode + " F"+feedrate+" \n"; //fixed feedrate 1200mm/min, 20mm/s

	while (i<xpath.length-1){
		i=i+1;
		gcode = gcode + "G1 X"+xpath[i];
		gcode = gcode + " Y" + ypath[i];
		gcode = gcode + " Z" + zpath[i];
		gcode = gcode + " E" + epath[i];
		gcode = gcode + " F"+feedrate+" \n"; //fixed feedrate 1200mm/min, 20mm/s
		}
	return gcode;
	}
