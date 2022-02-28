class Solidrectperimeter{
	constructor(x,y,xsize,ysize,radius,h,dr,dz,n,g,f,dir,estart){//n is segments per corner, g is extruder distance per travel, f is feedrate
		this.r=radius;
		this.h=h;
		this.dr=dr;
		if (this.r<this.dr*3){this.r=this.dr*3;}
		this.dz=dz;
		this.n=n;
		this.x=x;
		this.y=y;
		this.f=f;
		this.g=g;
		this.dir = dir;
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

		var roundperimeters = new Thickrectperimeter(this.x,this.y,this.xs,this.ys,this.r-2*this.dr,this.r,this.h,this.dr,this.dz,this.n,this.g,this.f,-1*this.dir,this.estart);
		this.xpath = this.xpath.concat(roundperimeters.xpath);//this.xpath = this.xpath.concat(currentperimeter.xpath)
		console.log(roundperimeters.xpath);
		this.ypath = this.ypath.concat(roundperimeters.ypath);
		this.zpath = this.zpath.concat(roundperimeters.zpath);
		this.epath = this.epath.concat(roundperimeters.epath);
		this.fpath = this.fpath.concat(roundperimeters.fpath);
	
		
		var corner1x = this.x+dx-0*this.dr;//This point is redundant but sets the extruder position to estart
		var corner1y = this.y-dy-0*this.dr; //instead of calculating by previous point.
		console.log("x "+corner1x+" y "+corner1y);
		this.xpath.push(corner1x);
		this.ypath.push(corner1y);
		this.zpath.push(this.h);
		this.epath.push(this.estart);
		this.fpath.push(this.f);
		
		var squirali = Math.floor(dx/this.dr);
		if (this.xs>this.ys){squirali = Math.floor(dy/this.dr);}
		var i=0;
		console.log(squirali);// why is this NaN
		while (i<squirali){//fix this to end when in center.
			var corner1x = this.x+dx-i*this.dr;
			var corner1y = this.y+dy-i*this.dr;
			var corner2x = this.x-dx+i*this.dr;
			var corner2y = this.y+dy-i*this.dr;
			var corner3x = this.x-dx+i*this.dr;
			var corner3y = this.y-dy+i*this.dr;
			var corner4x = this.x+dx-i*this.dr;
			var corner4y = this.y-dy+i*this.dr;
			
			this.xpath.push(corner4x);
			this.ypath.push(corner4y);
			this.zpath.push(this.h);
			var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
			this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
			this.fpath.push(this.f);
			
			this.xpath.push(corner1x);
			this.ypath.push(corner1y);
			this.zpath.push(this.h);
			var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
			this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
			this.fpath.push(this.f);
			
			this.xpath.push(corner2x);
			this.ypath.push(corner2y);
			this.zpath.push(this.h);
			var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
			this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
			this.fpath.push(this.f);
			
			this.xpath.push(corner3x);
			this.ypath.push(corner3y);
			this.zpath.push(this.h);
			var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
			this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
			this.fpath.push(this.f);
			//console.log(corner3x);
			//console.log(corner3y);
			i++;
			var seamx = this.x+dx-i*this.dr;
			var seamy = this.y-dy+i*this.dr;
			this.xpath.push(seamx);
			this.ypath.push(seamy);
			this.zpath.push(this.h);
			var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
			this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
			this.fpath.push(this.f);
			console.log(seamx);
			console.log(seamy);
			}
		}
	}