class Rectperimeter{
	constructor(x,y,xsize,ysize,radius,h,dr,dz,n,g,f,dir,estart){//n is segments per corner, g is extruder distance per travel, f is feedrate
		this.r=radius;
		this.h=h;
		this.dr=dr;
		this.dz=dz;
		this.n=n;
		this.x=x;
		this.y=y;
		this.f=f;
		this.g=g;
		this.dir = dir;
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
		//First point, middle of low Y face.
		this.xpath.push(this.x);
		this.ypath.push(this.y-this.ys/2);
		this.zpath.push(this.h);
		this.epath.push(estart);
		this.fpath.push(f);
		//2nd point, start of first rounded corner...  This is redundant with first corner i think
		this.xpath.push(this.x+dx);
		this.ypath.push(this.y-this.ys/2);
		this.zpath.push(this.h);
		var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
		this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
		this.fpath.push(f);

		var i=1;//First rounded corner starts here
		while(i<this.n){
			this.xpath.push(this.x+dx+(this.r)*Math.cos(i*0.5*Math.PI/n-Math.PI/2));
			this.ypath.push(this.y-dy+(this.r)*Math.sin(i*0.5*Math.PI/n-Math.PI/2));
			this.zpath.push(this.h);
			if (this.epath.length>0){var lastepath = this.epath[this.epath.length-1];}
			else {lastepath = estart;}
			var segdistance = (this.r)*0.5*Math.PI/n;
			this.epath.push(lastepath+segdistance*g);
			this.fpath.push(f);
			//if (i>(this.n-this.ht)){//Assumes somethingpath.length == i
			//	var ddr = this.dr/this.ht;//r difference per point
			//	var unnameable=i-(this.n-this.ht);
			//	this.xpath[i]=(this.x+(this.r+ddr*unnameable*dir)*Math.cos(i*2*Math.PI/n));
			//	this.ypath[i]=(this.y+(this.r+ddr*unnameable*dir)*Math.sin(i*2*Math.PI/n));	
			//	//console.log(this.r+ddr*unnameable*dir+" "+this.ht);
			//	}
			//if (i>(this.n-this.vt)){
			//	var ddz = this.dz/this.vt;//z difference per point
			//	var unnameable=i-(this.n-this.vt)
			//	this.zpath[i]=this.zpath[i]+ddz*unnameable;	
			//	}
			i++;
			}
		//Point at end of 1st corner
		this.xpath.push(this.x+this.xs/2);
		this.ypath.push(this.y-dy);
		this.zpath.push(this.h);
		var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
		this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
		this.fpath.push(f);
		//point at start of 2nd corner
		this.xpath.push(this.x+this.xs/2);
		this.ypath.push(this.y+dy);
		this.zpath.push(this.h);
		var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
		this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
		this.fpath.push(f);
		var i=1;//2nd rounded corner starts here
		while(i<this.n){
			this.xpath.push(this.x+dx+(this.r)*Math.cos(i*0.5*Math.PI/n));
			this.ypath.push(this.y+dy+(this.r)*Math.sin(i*0.5*Math.PI/n));
			this.zpath.push(this.h);
			if (this.epath.length>0){var lastepath = this.epath[this.epath.length-1];}
			else {lastepath = estart;}
			var segdistance = (this.r)*0.5*Math.PI/n;
			this.epath.push(lastepath+segdistance*g);
			this.fpath.push(f);
			i++;
			}
		//Point at end of 2nd corner
		this.xpath.push(this.x+dx);
		this.ypath.push(this.y+this.ys/2);
		this.zpath.push(this.h);
		var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
		this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
		this.fpath.push(f);
		//point at start of 3rd corner
		this.xpath.push(this.x-dx);
		this.ypath.push(this.y+this.ys/2);
		this.zpath.push(this.h);
		var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
		this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
		this.fpath.push(f);
		var i=1;//3rd rounded corner starts here
		while(i<this.n){
			this.xpath.push(this.x-dx+(this.r)*Math.cos(i*0.5*Math.PI/n+0.5*Math.PI));
			this.ypath.push(this.y+dy+(this.r)*Math.sin(i*0.5*Math.PI/n+0.5*Math.PI));
			this.zpath.push(this.h);
			if (this.epath.length>0){var lastepath = this.epath[this.epath.length-1];}
			else {lastepath = estart;}
			var segdistance = (this.r)*0.5*Math.PI/n;
			this.epath.push(lastepath+segdistance*g);
			this.fpath.push(f);
			i++;
			}	
		//Point at end of 3rd corner
		this.xpath.push(this.x-this.xs/2);
		this.ypath.push(this.y+dy);
		this.zpath.push(this.h);
		var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
		this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
		this.fpath.push(f);
		//point at start of 4th corner
		this.xpath.push(this.x-this.xs/2);
		this.ypath.push(this.y-dy);
		this.zpath.push(this.h);
		var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
		this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
		this.fpath.push(f);		
		var i=1;//4th rounded corner starts here
		while(i<this.n){
			this.xpath.push(this.x-dx+(this.r)*Math.cos(i*0.5*Math.PI/n+1.0*Math.PI));
			this.ypath.push(this.y-dy+(this.r)*Math.sin(i*0.5*Math.PI/n+1.0*Math.PI));
			this.zpath.push(this.h);
			if (this.epath.length>0){var lastepath = this.epath[this.epath.length-1];}
			else {lastepath = estart;}
			var segdistance = (this.r)*0.5*Math.PI/n;
			this.epath.push(lastepath+segdistance*g);
			this.fpath.push(f);
			i++;
			}
		var seamdr = this.dr;
		var seamdz = this.dz;
		if (seamdz>0){seamdr = 0;}
		
		//Point at end of 4th corner
		this.xpath.push(this.x-dx);
		this.ypath.push(this.y-this.ys/2);
		this.zpath.push(this.h);
		var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
		this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
		this.fpath.push(f);
		//Point at end of seam
		
		this.xpath.push(this.x);
		this.ypath.push(this.y-this.ys/2-seamdr*this.dir);
		this.zpath.push(this.h+seamdz);	
		var lastdistance = Math.sqrt((this.xpath[this.xpath.length-1]-this.xpath[this.xpath.length-2])^2+(this.ypath[this.ypath.length-1]-this.ypath[this.ypath.length-2])^2);
		this.epath.push(this.epath[this.epath.length-1]+lastdistance*g);
		this.fpath.push(f);		
		}
	}