
document.addEventListener("mousemove", mouseMoveHandler, false);
function mouseMoveHandler(e) {
	mousex = e.clientX;
	mousey =  e.clientY;
	mousedx = mousex-mousedownx;
	mousedy = mousey-mousedowny;
}
document.addEventListener("mousedown", mouseDownHandler, false);
function mouseDownHandler(e) {
	mousedownx = e.clientX;
	mousedowny = e.clientY;
	mousedx = 0;
	mousedy = 0;
    var inbounds = false;
	if (mousedownx>sidepreviewx){lefthand=false;}else{lefthand=true;}
	if ((mousex>0)&&(mousex<canvas.width)&&(mousey>0)&&(mousey<canvas.height)){ inbounds = true; }
    var mselect = document.getElementById("mselect").checked;
    if (mselect&&inbounds){
        //console.log("Input R and H"+-1*(mousedownx-sidepreviewx)/scale+" "+-1*(mousedowny-sidepreviewy)/scale);
        var cakepoint = currentcake.closestpoint(-1*(mousedownx-sidepreviewx)/scale,-1*(mousedowny-sidepreviewy)/scale);
		var dragid = document.getElementById("mdid").checked;
		var dragod = document.getElementById("mdod").checked;
		document.getElementById("mdod").checked = false;
		document.getElementById("mdid").checked = false;
		console.log(cakepoint);
		if (cakepoint[1]==0){ 
			document.getElementById("mdid").checked=true; 
			document.getElementById("mdod").checked=false;
		}else{
			document.getElementById("mdid").checked=false;
			document.getElementById("mdod").checked=true;
			}
        cakelevel = cakepoint[0];
        freshstagevalues();
        }
	if (mdrag&&inbounds){
        mousedragging = true;
		//console.log("mousedragging");
		}
	}
document.addEventListener("mouseup", mouseUpHandler, false);
function mouseUpHandler(e) {
	mousedragging = false;
	var mousedrag = document.getElementById("mdrag").checked;
	var inbounds = false;
	if ((mousex>0)&&(mousex<canvas.width)&&(mousey>0)&&(mousey<canvas.height)){ inbounds = true; }
	if (mousedrag&&inbounds){
		var dragid = document.getElementById("mdid").checked;
		var dragod = document.getElementById("mdod").checked;
		var dragh = document.getElementById("mdh").checked;
		if (partclass==0){
			if (dragid){
				cakeids[cakelevel]=cakeids[cakelevel]-mousedx/scale;
				if (cakeids[cakelevel]<0){ cakeids[cakelevel]=1; } //If ID is less than 0, set to 1 (mm)
				if (cakeids[cakelevel]>cakeods[cakelevel]){ cakeids[cakelevel]=cakeods[cakelevel]-1; } //If ID is less than 0, set to 1 (mm)
				}
			if (dragod){
				cakeods[cakelevel]=cakeods[cakelevel]-mousedx/scale; 
				if (cakeods[cakelevel]<cakeids[cakelevel]){ cakeods[cakelevel]=cakeids[cakelevel]+1 }//if OD is less than ID, set to ID+1
				}
			if (dragh){
				cakehs[cakelevel+1]=cakehs[cakelevel+1]-mousedy/scale; 
				if (cakehs[cakelevel+1]<cakehs[cakelevel]){ cakehs[cakelevel+1]=cakehs[cakelevel]+1 }//if height is less than previous height, set to previous height +1
				if (cakelevel+1<cakehs.length-1){	//If not on top layer (cakehs indexes are cakelevel+1)
					if (cakehs[cakelevel+1]>cakehs[cakelevel+2]){ cakehs[cakelevel+1]=cakehs[cakelevel+2]-1 }//if next height is less than height, set next to height +1
					}
				}
			}
		if (partclass==1){
			if (dragid){
				tcakeids[cakelevel]=tcakeids[cakelevel]-mousedx/scale;
				if (tcakeids[cakelevel]<0){ tcakeids[cakelevel]=1; } //If ID is less than 0, set to 1 (mm)
				if (tcakeids[cakelevel]>tcakeods[cakelevel]){ tcakeids[cakelevel]=tcakeods[cakelevel]-1; } //If ID is less than 0, set to 1 (mm)
				}
			if (dragod){
				tcakeods[cakelevel]=tcakeods[cakelevel]-mousedx/scale; 
				if (tcakeods[cakelevel]<tcakeids[cakelevel]){ tcakeods[cakelevel]=tcakeids[cakelevel]+1 }//if OD is less than ID, set to ID+1
				}
			if (dragh){
				tcakehs[cakelevel]=tcakehs[cakelevel]-mousedy/scale; 
				if (cakelevel>0){
					if (tcakehs[cakelevel]<tcakehs[cakelevel-1]){ tcakehs[cakelevel]=tcakehs[cakelevel-1]+1 }//if height is less than previous height, set to previous height +1
					}
				if (cakelevel<tcakehs.length-1){	//If not on top layer,
					if (tcakehs[cakelevel]>tcakehs[cakelevel+1]){ tcakehs[cakelevel]=tcakehs[cakelevel+1]-1 }//if next height is less than height, set next to height +1
					}
				}
			}
		freshcake();
		freshstagevalues();
		}
	}