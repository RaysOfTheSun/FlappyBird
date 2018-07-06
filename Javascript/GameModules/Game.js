let bird;
let pipeCollection;
let playerPoints;
let backdrop;
let ground;
let scoreboard;
let flappybirdFont;

function preload() {
    flappybirdFont = loadFont("res/Fonts/04B_19.ttf");
}

function setup() {
    createCanvas(innerWidth, innerHeight);
    pipeCollection = [new PipeSet()];
    playerPoints = 0;

    ground = new Ground();
    backdrop = new Backdrop(ground.offset);
    bird = new Bird(ground.offset, innerWidth/2)
    scoreboard = new Scoreboard();

    textFont(flappybirdFont);
    frameRate(60);
}

function draw() { 

    // erase everything in the canvas before redrawing so 
    // new stuff won't overlap with old stuff
    cleanCanvas();

    makePipes();
    for(let i = 0; i < pipeCollection.length; i++) {
        pipeCollection[i].toCanvas();
        pipeCollection[i].scroll(3);
    }

    if (pipeCollection[0].x_coordinate <= 0) {
        pipeCollection.shift();
    }

    if (pipeCollection[0].collide(bird)) {
        print("hit!")
    }
    else if (pipeCollection[0].isCleared(bird)) {
        playerPoints += 1;
    }

    scoreboard.toCanvas(playerPoints);

    bird.toCanvas();

    ground.toCanvas();
}

function cleanCanvas() {
    background("#71C5CF");   // Set the background to some shade of blue
    backdrop.toCanvas()
}

function keyPressed() {
    bird.jump();
}

function mouseClicked() {
    bird.jump();
}

// Creates a new PipeSet object that will serve as an obstacle in the game
function makePipes() {
    if (frameCount % 80 == 0) {
        pipeCollection.push(new PipeSet());
    }
}

function let_bird_fall() {
    while ((bird.y_coordinate != bird.lowerLimit) || (frameCount % 20 != 0)) {

    }
}