let bird;
let pipeCollection;
let playerPoints;
let backdrop;
let ground;

function setup() {
    createCanvas(600, 800);
    bird = new Bird(100, height/2)
    pipeCollection = [new PipeSet()];
    playerPoints = 0;

    ground = new Ground();
    backdrop = new Backdrop(ground.offset);
    frameRate(60);
}

function draw() { 
    cleanCanvas();

    makePipes();
    for(let i = 0; i < pipeCollection.length; i++) {
        pipeCollection[i].toCanvas();
        pipeCollection[i].scroll();
    }

    if (pipeCollection[0].x_coordinate <= 0) {
        pipeCollection.shift();
    }

    if (pipeCollection[0].collide(bird)) {
        console.log("FALL!");
    }
    else if (pipeCollection[0].isCleared(bird)) {
        playerPoints += 1;
    }

    bird.toCanvas();

    ground.toCanvas();
}

function cleanCanvas() {
    background(0);   // Set the background to black
    backdrop.toCanvas()
}

function keyPressed() {
    bird.jump();
}

// Creates a new PipeSet object that will serve as an obstacle in the game
function makePipes() {
    if (frameCount % 60 == 0) {
        pipeCollection.push(new PipeSet());
    }
}

function let_bird_fall() {
    while ((bird.y_coordinate != bird.lowerLimit) || (frameCount % 20 != 0)) {

    }
}