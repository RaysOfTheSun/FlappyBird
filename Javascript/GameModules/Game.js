let bird;

function setup() {
    createCanvas(720, 400);
    bird = new Bird(0, height/2)
    frameRate(60);
}

function draw() { 
    background(0);   // Set the background to black
    bird.toCanvas()
}

function keyPressed() {
    bird.jump();
}