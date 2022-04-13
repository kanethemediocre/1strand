class Cake{
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
		var firstbushing = new Bushing(this.x,this.y,this.ids[0],this.ods[0],this.hs[0],this.hs[1],this.dr,this.dz,this.n,this.g,this.f,this.dir,this.estart,this.ht,this.vt);//constructor(x,y,r1,r2,h1,h2,dr,dz,n,g,f,dir,estart,ht,vt){
		this.xpath = this.xpath.concat(firstbushing.xpath);
		this.ypath = this.ypath.concat(firstbushing.ypath);
		this.zpath = this.zpath.concat(firstbushing.zpath);
		this.epath = this.epath.concat(firstbushing.epath);
		this.fpath = this.fpath.concat(firstbushing.fpath);
		var i=1;
		var nexte = this.epath[this.epath.length-1];
		while(i<this.ids.length){
			var thedir = 1;
			var avgrad = (this.ids[i]+this.ods[i])/2;
			if (avgrad<this.xpath[this.xpath.length-1]-this.x){thedir = -1;}
			var nextbushing = new Bushing(this.x,this.y,this.ids[i],this.ods[i],this.hs[i],this.hs[i+1],this.dr,this.dz,this.n,this.g,this.f,thedir,nexte,this.ht,this.vt);
			this.xpath = this.xpath.concat(nextbushing.xpath);
			this.ypath = this.ypath.concat(nextbushing.ypath);
			this.zpath = this.zpath.concat(nextbushing.zpath);
			this.epath = this.epath.concat(nextbushing.epath);
			this.fpath = this.fpath.concat(nextbushing.fpath);
			var nexte = this.epath[this.epath.length-1];
			console.log("loopinyo");
			i++;
			}
		}
	exportasarray(){
			return [this.xpath,this.ypath,this.zpath,this.epath,this.fpath];
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
				idcolor = "red";
				}
			if (this.ods[i]>largestod){
				largestod = this.ods[i];
				odcolor = "red";
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
		var ts = thescale;
		context.strokeStyle="red";
		context.beginPath();
		context.rect(originx+this.ids[0]*ts,originy-this.hs[0]*ts,(this.ods[0]-this.ids[0])*ts,(this.hs[0]-this.hs[1])*ts);
		context.rect(originx-this.ods[0]*ts,originy-this.hs[0]*ts,(this.ods[0]-this.ids[0])*ts,(this.hs[0]-this.hs[1])*ts);
		//context.moveTo(originx,originy);//This is axis of the bushing.
		//context.lineTo(originx,originy-200);
		context.stroke();
		var i=1;
		while(i<this.ids.length){
			context.beginPath();
			context.rect(originx+this.ids[i]*ts,originy-this.hs[i]*ts,(this.ods[i]-this.ids[i])*ts,(this.hs[i]-this.hs[i+1])*ts);
			context.rect(originx-this.ods[i]*ts,originy-this.hs[i]*ts,(this.ods[i]-this.ids[i])*ts,(this.hs[i]-this.hs[i+1])*ts);
			context.stroke();
			i++;
			}
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
			var dh = this.hs[i+1]-inputh;
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
		return [closesti,closesttype,closestdistance];
		}
	}