class Bushing{
	constructor(x,y,r1,r2,h1,h2,dr,dz,n,g,f,dir,estart,ht,vt){
		this.x=x;
		this.y=y;
		this.r1=r1;
		this.r2=r2;
		this.h1=h1;
		this.h2=h2;
		this.dr=dr;
		this.dz=dz;
		this.n=n;
		this.g=g;
		this.f=f;
		this.dir = dir; 
		this.xpath = [];
		this.ypath = [];
		this.zpath = [];
		this.epath = [];
		this.fpath = [];
		var thedir = dir;
		var h = this.h1;
		console.log("first e"+estart);
		while(h<this.h2){
			if (this.epath.length>0){var es = this.epath[this.epath.length-1];}
			else{var es = estart;}
			var newdisc = new Disc(this.x,this.y,this.r1,this.r2,h,this.dr,this.dz,this.n,this.g,this.f,dir,es,ht,vt); //constructor(x,y,r1,r2,h,dr,dz,n,g,f,dir,estart,ht,vt){//n is segments per "circle", g is extruder distance per travel, f is feedrate
			this.xpath = this.xpath.concat(newdisc.xpath);
			this.ypath = this.ypath.concat(newdisc.ypath);
			this.zpath = this.zpath.concat(newdisc.zpath);
			this.epath = this.epath.concat(newdisc.epath);
			this.fpath = this.fpath.concat(newdisc.fpath);
			var si= this.xpath.length-Math.floor(this.n/2);//si = sample index
			var samplex = this.xpath[si]-centerx;
			var sampley = this.ypath[si]-centery;
			var achievedr1 = Math.sqrt(samplex*samplex+sampley*sampley); 
			//console.log("Achieved r1 "+achievedr1);//this is not accurate, not sure why.
			h=h+dz;
			if (h<this.h2){//Alternates dir between 1 and -1, so that discs alternate from inside out to outside in, improving continuity
				var es = this.epath[this.epath.length-1];
				var newdisc = new Disc(this.x,this.y,this.r1,this.r2,h,this.dr,this.dz,this.n,this.g,this.f,dir*-1,es,ht,vt);
				this.xpath = this.xpath.concat(newdisc.xpath);
				this.ypath = this.ypath.concat(newdisc.ypath);
				this.zpath = this.zpath.concat(newdisc.zpath);
				this.epath = this.epath.concat(newdisc.epath);
				this.fpath = this.fpath.concat(newdisc.fpath);
				var si= this.xpath.length-Math.floor(this.n/2);//si = sample index
				var samplex = this.xpath[si]-centerx;
				var sampley = this.ypath[si]-centery;
				var achievedr2 = Math.sqrt(samplex*samplex+sampley*sampley); 
				//console.log("Achieved r2 "+achievedr2);
				h=h+dz;
			}
		}
	}
	exportasarray(){
		return [this.xpath,this.ypath,this.zpath,this.epath,this.fpath];
	}
}