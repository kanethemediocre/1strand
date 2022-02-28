class Thickrectperimeter{
	constructor(x,y,xsize,ysize,numthick,radius,h,dr,dz,n,g,f,dir,estart){//n is segments per corner, g is extruder distance per travel, f is feedrate
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
		this.t=numthick;//number of perimeters.
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
		console.log("starting thickrectperimeter...");
		if (this.dir==1){
			var currentradius = this.r- this.t*this.dr;//8-5*1=3 OK
			var currentxsize = this.xs-this.t*this.dr*2; //30-8*2=14 Checks out not OK
			var currentysize = this.ys-this.t*this.dr*2;
			var maxradius = this.r;
			var currente = estart;
			while (currentradius<=maxradius){
				var seamdz = 0;
				if (currentradius+this.dr>maxradius){
					seamdz = this.dz;
					}
				console.log("requesting xs = "+currentxsize+" ys = "+currentysize+" r = "+currentradius);
				var currentperimeter = new Rectperimeter(this.x,this.y,currentxsize,currentysize,currentradius,this.h,this.dr,seamdz,8,0.1,1200,1,currente);//	constructor(x,y,xsize,ysize,radius,h,dr,dz,n,g,f,dir,estart){//
				this.xpath = this.xpath.concat(currentperimeter.xpath);
				this.ypath = this.ypath.concat(currentperimeter.ypath);
				this.zpath = this.zpath.concat(currentperimeter.zpath);
				this.epath = this.epath.concat(currentperimeter.epath);
				this.fpath = this.xpath.concat(currentperimeter.fpath);
				currente = this.epath[this.epath.length-1];
				currentradius = currentradius + this.dr;
				currentxsize = currentxsize+this.dr*2;
				currentysize = currentysize+this.dr*2;
				}
		}else if (this.dir==-1){
			
			var currentradius = this.r;
			var currentxsize = this.xs;
			var currentysize = this.ys;
			var minradius = this.r-this.t*this.dr;
			var currente = estart;
			while (currentradius>=minradius){
				var seamdz = 0;
				if (currentradius-this.dr<minradius){
					seamdz = this.dz;
					}
				console.log("requesting xs = "+currentxsize+" ys = "+currentysize+" r = "+currentradius);
				var currentperimeter = new Rectperimeter(this.x,this.y,currentxsize,currentysize,currentradius,this.h,this.dr,seamdz,8,0.1,1200,-1,currente);
				this.xpath = this.xpath.concat(currentperimeter.xpath);
				this.ypath = this.ypath.concat(currentperimeter.ypath);
				this.zpath = this.zpath.concat(currentperimeter.zpath);
				this.epath = this.epath.concat(currentperimeter.epath);
				this.fpath = this.xpath.concat(currentperimeter.fpath);
				currente = this.epath[this.epath.length-1];
				currentradius = currentradius - this.dr;
				currentxsize = currentxsize-this.dr*2;
				currentysize = currentysize-this.dr*2;
				}
			}
		}
	}