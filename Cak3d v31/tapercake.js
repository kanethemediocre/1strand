class TaperCake{
	constructor(x,y,ids,ods,hs,dr,dz,n,g,f,dir,estart,ht,vt){//ids, ods, and hs are arrays of id, od, and height.
		this.x=x;
		this.y=y;
		this.ids=ids;
		this.ods=ods;
		this.hs=hs;
		this.dr=dr;
		this.dz=dz;
		this.n=n;
		this.g=g;
		this.f=f;
		this.dir=dir;
		this.estart=estart;
		this.ht=ht;
		this.vt=vt;
		this.xpath = [];
		this.ypath = [];
		this.zpath = [];
		this.epath = [];
		this.fpath = [];
		var es = this.estart;
		var i=1;
		while(i<ids.length){
			var thedir = this.dir;
			var avgrad = (this.ids[i]+this.ods[i])/2;
			if (this.xpath.length>0){
				if (avgrad<this.xpath[this.xpath.length-1]-this.x){thedir = -1;}
				else {thedir = 1;}
				}
			var nextbushing = new TaperBushing(this.x,this.y,this.ids[i-1],this.ids[i],this.ods[i-1],this.ods[i],this.hs[i-1],this.hs[i],this.dr,this.dz,this.n,this.g,this.f,thedir,es,this.ht,this.vt);
			this.xpath = this.xpath.concat(nextbushing.xpath);
			this.ypath = this.ypath.concat(nextbushing.ypath);
			this.zpath = this.zpath.concat(nextbushing.zpath);
			this.epath = this.epath.concat(nextbushing.epath);
			this.fpath = this.xpath.concat(nextbushing.fpath);
			es = this.epath[this.epath.length-1];
			i++;
			}
		}
	exportasarray(){
		return [this.xpath,this.ypath,this.zpath,this.epath,this.fpath];
		}
	draw3d(originx,originy,thescale,time){//Stuck in red and blue for now.
		var endi=this.xpath.length-1;
		var i = 1;
		while(i<endi){
			var thered = Math.floor(255 - 255*(i/this.xpath.length));
			var theblue = Math.floor(255*(i/this.xpath.length));
			var thecolor = "rgb(" + thered + ",0," + theblue + ")";
			draw3dline(this.xpath[i],this.ypath[i],this.zpath[i],this.xpath[i-1],this.ypath[i-1],this.zpath[i-1],originx,originy,thescale,thecolor)//Isometric view, where 1 unit of X, Y, and Z distance are equal on the scree
			i++;
			}
		}
	draw2dtop(originx,originy,thescale,time){
		var i = this.ids.length;
		var idcolor = "brown";
		var odcolor = "brown";
		var smallestid = 999999;
		var largestod = 0;
		while(i>0){
			i--;
			if (this.ids[i]<smallestid){
				smallestid = this.ids[i];
				idcolor = "yellow";
				}
			if (this.ods[i]>largestod){
				largestod = this.ods[i];
				odcolor = "yellow";
				}
			context.strokeStyle = idcolor;
			context.beginPath()
			context.arc(originx,originy, this.ids[i]*thescale, 0, 2 * Math.PI, false); //draws the circle
			context.stroke();
			context.strokeStyle = odcolor;
			context.beginPath()
			context.arc(originx,originy, this.ods[i]*thescale, 0, 2 * Math.PI, false); //draws the circle
			context.stroke();
			}
		}
	draw2dside(originx,originy,thescale,time){
		context.strokeStyle="red";
		var i=1;
		while(i<this.ids.length){
			context.beginPath();
			context.moveTo(originx+this.ids[i-1]*thescale,originy-this.hs[i-1]*thescale);
			context.lineTo(originx+this.ods[i-1]*thescale,originy-this.hs[i-1]*thescale);
			context.lineTo(originx+this.ods[i]*thescale,originy-this.hs[i]*thescale);
			context.lineTo(originx+this.ids[i]*thescale,originy-this.hs[i]*thescale);
			context.lineTo(originx+this.ids[i-1]*thescale,originy-this.hs[i-1]*thescale);
			context.stroke();

			context.beginPath();
			context.moveTo(originx-this.ids[i-1]*thescale,originy-this.hs[i-1]*thescale);
			context.lineTo(originx-this.ods[i-1]*thescale,originy-this.hs[i-1]*thescale);
			context.lineTo(originx-this.ods[i]*thescale,originy-this.hs[i]*thescale);
			context.lineTo(originx-this.ids[i]*thescale,originy-this.hs[i]*thescale);
			context.lineTo(originx-this.ids[i-1]*thescale,originy-this.hs[i-1]*thescale);
			context.stroke();
			i++;
			}
		}
	animate(originx,originy,thescale,speed,length,thecolor,time){
		var endi=time*speed+length;
		var i = time*speed;
		while(i<endi){
			draw3dline(this.xpath[i],this.ypath[i],this.zpath[i],this.xpath[i-1],this.ypath[i-1],this.zpath[i-1],originx,originy,thescale,thecolor)//Isometric view, where 1 unit of X, Y, and Z distance are equal on the scree
			i++;
			}
		}
	closestpoint(inputr,inputh){
		var i=0;
		var closesttype = 0; //1 will symbolize an OD, 0 ID.
		var closestdistance = 999999;
		var closesti = 0;
		while (i<this.ids.length){
			var dr1 = this.ids[i]-inputr;
			var dr2 = this.ods[i]-inputr;
			var dh = this.hs[i]-inputh;
			var iddistance = Math.sqrt(dr1*dr1+dh*dh);
			var oddistance = Math.sqrt(dr2*dr2+dh*dh);
			if (iddistance<closestdistance){
				closesti = i;
				closestdistance = iddistance;
				closesttype = 0;
				}
			if (oddistance<closestdistance){
				closesti = i;
				closestdistance = oddistance;
				closesttype = 1;
				}
			i++;
			}
			console.log(dr1+" "+dr2+" "+dh)
		return [closesti,closesttype,closestdistance];
		}
	}