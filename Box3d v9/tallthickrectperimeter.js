class Tallthickrectperimeter{
	constructor(x,y,xsize,ysize,numthick,radius,h1,h2,dr,dz,n,g,f,dir,estart){//n is segments per corner, g is extruder distance per travel, f is feedrate
		this.r=radius;
		this.h1=h1;
		this.h2=h2;
		this.dr=dr;
		this.dz=dz;
		this.n=n;
		this.x=x;
		this.y=y;
		this.f=f;
		this.g=g;
		this.dir = dir;
		this.t=numthick;//number of perimeters.
		this.estart = estart;
		this.xs = xsize;
		this.ys = ysize;
		this.xpath = [];
		this.ypath = [];
		this.zpath = [];
		this.epath = [];
		this.fpath = [];
		var dx = this.xs/2-this.r; //location for corner radius center relative to absolute center
		var dy = this.ys/2-this.r;
		var x1 = this.x+dx;
		var y1 = this.y+dy;
		var x2 = this.x-dx;
		var y2 = this.y+dy;
		var x3 = this.x-dx;
		var y3 = this.y-dy;
		var x4 = this.x+dx;
		var y4 = this.y-dy;
		console.log("starting tallthickrectperimeter...");
		var currentheight=this.h1;
		console.log("height = "+currentheight);
		
		var currentdir = this.dir;
		while (currentheight<this.h2){
			console.log("Made it in the while loop");
			var layer = new Thickrectperimeter(this.x,this.y,this.xs,this.ys,this.t,this.r,currentheight,this.dr,this.dz,this.n,this.g,this.f,this.dir,this.estart);
			this.xpath = this.xpath.concat(layer.xpath);//this.xpath = this.xpath.concat(currentperimeter.xpath)
			console.log(layer.xpath);
			this.ypath = this.ypath.concat(layer.ypath);
			this.zpath = this.zpath.concat(layer.zpath);
			this.epath = this.epath.concat(layer.epath);
			this.fpath = this.fpath.concat(layer.fpath);
			//var testbox2 = new Thickrectperimeter(centerx,centery,30,60,5,8,0,1,6.5,8,0,1200,1,0)//constructor(x,y,xsize,ysize,numthick,radius,h,dr,dz,n,g,f,dir,estart){
			currentdir = currentdir * -1;
			currentheight = currentheight+this.dz;
			}
		if (this.dir==1){

		}else if (this.dir==-1){

			}
		}
	}