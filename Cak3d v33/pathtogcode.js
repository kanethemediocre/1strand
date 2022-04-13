function pathtogcode(paths){
	var xpath = paths[0];
	var ypath = paths[1];
	var zpath = paths[2];
	var epath = paths[3];
	var fpath = paths[4];
	var gcode = "G28 \nG21 \nG90 \nG92 E0 \nM82";
	var i=0
	gcode = gcode + "G1 X"+xpath[0];
	gcode = gcode + " Y" + ypath[0];
	gcode = gcode + " Z" + zpath[0];
	gcode = gcode + " E" + epath[0];
	gcode = gcode + " F"+fpath[0]+" \n"; //fixed feedrate 1200mm/min, 20mm/s

	while (i<xpath.length-1){
		i=i+1;
		gcode = gcode + "G1 X"+xpath[i];
		gcode = gcode + " Y" + ypath[i];
		gcode = gcode + " Z" + zpath[i];
		gcode = gcode + " E" + epath[i];
		gcode = gcode + " F"+fpath[i]+" \n"; //fixed feedrate 1200mm/min, 20mm/s
		}
	return gcode;
}