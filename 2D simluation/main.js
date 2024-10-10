const canvas = document.getElementById("myCanvas");

canvas.width=200;

//Ctx is a tool used to draw, here we call its context by calling 2D
const ctx = canvas.getContext("2d");

const road=new Road(canvas.width/2,canvas.width)
//x,y,width,height
const car = new Car(100,100,30,50);
car.draw(ctx); //function

animate();

function animate(){
    car.update();
    canvas.height=window.innerHeight;
    // road.draw(ctx);
    car.draw(ctx);
    requestAnimationFrame(animate);
}