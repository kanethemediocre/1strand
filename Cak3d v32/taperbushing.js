class TaperBushing{
	constructor(x,y,id1,id2,od1,od2,h1,h2,dr,dz,n,g,f,dir,estart,ht,vt){
		this.x=x;
		this.y=y;
		this.id1=id1;
		this.id2=id2;
		this.od1=od1;
		this.od2=od2;
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
		var skip=false;
		if (h1==h2){
			skip=true;//If a tapered bushing has no height change, it has no volume.  No printing needs to be done for it.  This will happen when there is horizontal surface.
		}else{
			var idslopeinv = (id2-id1)/(h2-h1);//REQUIRES height change to avoid /0.  This is preferable to requiring a id and od change.
			var odslopeinv = (od2-od1)/(h2-h1);
			}
		var thedir = dir;
		var h = this.h1;
		console.log("first e"+estart);
		while((h<this.h2)&&(!skip)){
			var localheight = h-this.h1;
			var idradius = id1+localheight*idslopeinv; 
			var odradius = od1+localheight*odslopeinv; 
			if (this.epath.length>0){var es = this.epath[this.epath.length-1];}
			else{var es = estart;}
			var newdisc = new Disc(this.x,this.y,idradius,odradius,h,this.dr,this.dz,this.n,this.g,this.f,dir,es,ht,vt);
			this.xpath = this.xpath.concat(newdisc.xpath);
			this.ypath = this.ypath.concat(newdisc.ypath);
			this.zpath = this.zpath.concat(newdisc.zpath);
			this.epath = this.epath.concat(newdisc.epath);
			this.fpath = this.xpath.concat(newdisc.fpath);
			var si= this.xpath.length-Math.floor(this.n/2);//si = sample index
			var samplex = this.xpath[si]-centerx;
			var sampley = this.ypath[si]-centery;
			var achievedr1 = Math.sqrt(samplex*samplex+sampley*sampley); 
			//console.log("Achieved r1 "+achievedr1);//this is not accurate, not sure why.
			h=h+dz;
			if (h<this.h2){//Alternates dir between 1 and -1, so that discs alternate from inside out to outside in, improving continuity
				var localheight = h-this.h1;
				var idradius = id1+localheight*idslopeinv; 
				var odradius = od1+localheight*odslopeinv; 
				var es = this.epath[this.epath.length-1];
				var newdisc = new Disc(this.x,this.y,idradius,odradius,h,this.dr,this.dz,this.n,this.g,this.f,dir*-1,es,ht,vt);
				this.xpath = this.xpath.concat(newdisc.xpath);
				this.ypath = this.ypath.concat(newdisc.ypath);
				this.zpath = this.zpath.concat(newdisc.zpath);
				this.epath = this.epath.concat(newdisc.epath);
				this.fpath = this.xpath.concat(newdisc.fpath);
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