class Disc{
	constructor(x,y,r1,r2,h,dr,dz,n,g,f,dir,estart,ht,vt){//n is segments per "circle", g is extruder distance per travel, f is feedrate
		this.x=x;
		this.y=y;
		var realr1 = -999
		var realr2 = -999
		if (r1<r2){ //Corrects R1 to always be the small radius.
			realr1=r1;
			realr2=r2;
		}else{
			realr1=r2;
			realr2=r1;
		}
		this.r1=realr1;
		this.r2=realr2;
		this.h=h;
		this.dr=dr;
		this.dz=dz;
		this.n=n;
		this.g=g;
		this.f=f;
		this.ht=ht;
		this.vt=vt;
		this.xpath = [];
		this.ypath = [];
		this.zpath = [];
		this.epath = [];
		this.fpath = [];
		this.dir = dir; 
		var r= this.r1+this.dr/2;; //inside out if dir==1
		var endr = this.r2-this.dr/2;//end at outside if dir==1
		if (this.dir<0){
			r=this.r2-this.dr/2; //outside in if dir==-1.
			endr=this.r1+this.dr/2;//end at inside if dir==-1
			}//end at inside if dir==-1
		while(dir*r<dir*endr){//Loop runs while r<endr if dir==1, runs while r>endr if dir==-1
			var nextr = r+dir*this.dr;
			var thisvt = 0;
			var thisht = ht; //Execute horizontal transition but not vertical
			if (dir*nextr>dir*endr){//If this is the last perimeter on the disc
				thisvt = vt;
				thisht = 0; //Execute vertical transition but not horizontal
				}
			if (this.epath.length>0){var es = this.epath[this.epath.length-1];}
			else{var es = estart;}
			var newperimeter = new Discperimeter(this.x,this.y,r,this.h,this.dr,this.dz,this.n,this.g,this.f,dir,es,thisht,thisvt);
			this.xpath = this.xpath.concat(newperimeter.xpath);
			this.ypath = this.ypath.concat(newperimeter.ypath);
			this.zpath = this.zpath.concat(newperimeter.zpath);
			this.epath = this.epath.concat(newperimeter.epath);
			this.fpath = this.xpath.concat(newperimeter.fpath);
			r=r+dir*this.dr;
			}
		}
	}