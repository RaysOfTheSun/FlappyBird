let bird;
let pipeCollection;
let playerPoints;
let backdrop;
let ground;
let scoreboard;
let flappybirdFont;
let currentPipe;
let hasPipeReadyForDeletion;

function preload() {
    flappybirdFont = loadFont("./res/Fonts/04B_19.TTF");
    ground = new Ground();
    backdrop = new Backdrop(ground.offset);
    bird = new Bird(ground.offset, innerWidth/2);
}

function setup() {
    
    createCanvas(innerWidth, innerHeight);
    scoreboard = new Scoreboard();
    
    pipeCollection = [new PipeSet()];
    currentPipe = pipeCollection[0];

    playerPoints = 0;
    
    frameRate(60);
    textFont(flappybirdFont, 100);
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
        hasPipeReadyForDeletion = true;
        shufflePipes();
    }

    if (pipeCollection[0].collide(bird)) {
        print("hit!")
    }
    else if (pipeCollection[0].isCleared(bird)) {
        playerPoints += 1;
        scoreboard.buzz();
    }

    scoreboard.toCanvas(playerPoints);

    bird.toCanvas();

    ground.toCanvas();

    print(pipeCollection.length);
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

function touchStarted() {
    bird.jump();
    return false;
}

// Creates a new PipeSet object that will serve as an obstacle in the game
function makePipes() {
    if ((frameCount % 80 == 0 && !hasPipeReadyForDeletion) && (pipeCollection.length < Math.floor(innerWidth / 80))) {
        pipeCollection.push(new PipeSet());
        print("new!");
    }
}

function shufflePipes() {
    if (frameCount % 80 == 0) {
        pipeCollection.push(currentPipe);
        pipeCollection[pipeCollection.length - 1].calculateDimensions();
        pipeCollection[pipeCollection.length - 1].cleared = false;
    }
    pipeCollection.shift();
    currentPipe = pipeCollection[0];
    hasPipeReadyForDeletion = false;
}

function let_bird_fall() {
    while ((bird.y_coordinate != bird.lowerLimit) || (frameCount % 20 != 0)) {

    }
}