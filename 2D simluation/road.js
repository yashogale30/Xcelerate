class Road{
    constructor(x,width,lanecount=3){
        this.x=x;
        this.width=width;
        this.lanecount=lanecount;
        this.left=x-width/2;
        this.right=x+width/2;

        const infinity = 100000000000;
        this.top = -infinity;
        this.bottom=infinity;


    }

    draw(ctx){
        ctx.lineWidth=5;
        ctx.strokesStyle="white";

        ctx.beginPath();
        ctx.moveTo(this.left,this.top);
        ctx.lineTo(this.left,this.bottom)
        ctx.stoke();

        ctx.beginPath();
        ctx.moveTo(this.right,this.top);
        ctx.lineTo(this.right,this.bottom)
        ctx.stoke();
    }


}