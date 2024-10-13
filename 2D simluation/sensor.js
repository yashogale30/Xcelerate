class Sensor{
    constructor(car){
        //generating rays of sensors
        this.car=car;
        this.rayCount=5;
        this.rayLength=150;
        this.raySpread=Math.PI/2;

        this.rays=[];
        this.readings=[];
    }

    //updating the sensor by casting rays
    update(roadBorders,traffic){
        this.#castRays();
        this.readings=[];//resets the array for new ones
        for(let i=0;i<this.rays.length;i++){
            this.readings.push(
                this.#getReading(
                    this.rays[i],
                    roadBorders,
                    traffic
                )
            );
        }
    }

    #getReading(ray,roadBorders,traffic){
        let touches=[];


        //intersection with roadborders
        for(let i=0;i<roadBorders.length;i++){
            const touch=getIntersection(//getintersection , if it hits its overlaps
                ray[0],
                ray[1],
                roadBorders[i][0],
                roadBorders[i][1]
            );
            if(touch){
                touches.push(touch);
            }
        }


        //intersection with other cars. we used polygon structure
        for(let i=0;i<traffic.length;i++){
            const poly=traffic[i].polygon;
            for(let j=0;j<poly.length;j++){
                const value=getIntersection(
                    ray[0],
                    ray[1],
                    poly[j],
                    poly[(j+1)%poly.length]
                );
                if(value){
                    touches.push(value);
                }
            }
        }

        if(touches.length==0){
            return null;
        }else{
            const offsets=touches.map(e=>e.offset);
            const minOffset=Math.min(...offsets);
            return touches.find(e=>e.offset==minOffset);//return the miniumum offset value
        }
    }

    #castRays(){
        //here we use trignometry and maths to cast rays 
        this.rays=[];
        for(let i=0;i<this.rayCount;i++){
            const rayAngle=lerp(
                this.raySpread/2,
                -this.raySpread/2,
                this.rayCount==1?0.5:i/(this.rayCount-1)
            )+this.car.angle;

            const start={x:this.car.x, y:this.car.y};
            const end={
                x:this.car.x-
                    Math.sin(rayAngle)*this.rayLength,
                y:this.car.y-
                    Math.cos(rayAngle)*this.rayLength
            };
            this.rays.push([start,end]);
        }
    }

    draw(ctx){
        //here we draw the sensor to the canvas
        for(let i=0;i<this.rayCount;i++){
            let end=this.rays[i][1];// Default end point of the ray
            
            // If a reading (obstacle) was found, set the end point to the intersection point
            if(this.readings[i]){
                end=this.readings[i];
            }

            ctx.beginPath();
            ctx.lineWidth=2;
            ctx.strokeStyle="yellow";
            ctx.moveTo(
                this.rays[i][0].x,
                this.rays[i][0].y
            );
            ctx.lineTo(
                end.x,
                end.y
            );
            ctx.stroke();

            ctx.beginPath();
            ctx.lineWidth=2;
            ctx.strokeStyle="black";//the black overlapped path
            ctx.moveTo(
                this.rays[i][1].x,
                this.rays[i][1].y
            );
            ctx.lineTo(
                end.x,
                end.y
            );
            ctx.stroke();
        }
    }        
}