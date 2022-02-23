class Discperimeter{
	constructor(x,y,r,h,dr,dz,n,g,f,dir,estart,ht,vt){//n is segments per "circle", g is extruder distance per travel, f is feedrate
		this.r=r;
		this.h=h;
		this.dr=dr;
		this.dz=dz;
		this.n=n;
		this.ht=ht;
		this.vt=vt;
		this.x=x;
		this.y=y;
		this.xpath = [];
		this.ypath = [];
		this.zpath = [];
		this.epath = [];
		this.fpath = [];
		var i=0;
		while(i<this.n){
			this.xpath.push(this.x+(this.r)*Math.cos(i*2*Math.PI/n));
			this.ypath.push(this.y+(this.r)*Math.sin(i*2*Math.PI/n));
			this.zpath.push(this.h);
			if (this.epath.length>0){var lastepath = this.epath[this.epath.length-1];}
			else {lastepath = estart;}
			var segdistance = (this.r)*2*Math.PI/n;
			this.epath.push(lastepath+segdistance*g);
			this.fpath.push(f);
			if (i>(this.n-this.ht)){//Assumes somethingpath.length == i
				var ddr = this.dr/this.ht;//r difference per point
				var unnameable=i-(this.n-this.ht);
				this.xpath[i]=(this.x+(this.r+ddr*unnameable*dir)*Math.cos(i*2*Math.PI/n));
				this.ypath[i]=(this.y+(this.r+ddr*unnameable*dir)*Math.sin(i*2*Math.PI/n));	
				//console.log(this.r+ddr*unnameable*dir+" "+this.ht);
				}
			if (i>(this.n-this.vt)){
				var ddz = this.dz/this.vt;//z difference per point
				var unnameable=i-(this.n-this.vt)
				this.zpath[i]=this.zpath[i]+ddz*unnameable;	
				}
			i++;
			}	
		}
	}