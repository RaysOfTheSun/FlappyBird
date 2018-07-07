let flappybirdFont; /* the font to be used in rendering text anywhere in the
                    game world */

let backdrop; // the game world's background
let ground; // the game world's visual lower boundary
let scoreboard; /* the number in the middle upper part of the screen
                showing the player's score */

let bird; // Flappy Bird
let pipeCollection; // The array where the obstacles in the game are stored
let currentPipe; // the pipeSet object that is directly infront of the bird object
let hasPipeInQueueForShift;
let maxNumberOfPipes;


let isPlayerDead;
let playerPoints; // The number of points the user has earned

function preload() {
    flappybirdFont = loadFont("./res/Fonts/04B_19.TTF");
    ground = new Ground();
    backdrop = new Backdrop(ground.offset);
    bird = new Bird(ground.offset, innerWidth/2);
}

function setup() {
    
    createCanvas(innerWidth, innerHeight);
    
    maxNumberOfPipes = (Math.floor(innerWidth / 80) / 3);
    isPlayerDead = false;

    scoreboard = new Scoreboard();
    pipeCollection = [new PipeSet()];
    currentPipe = pipeCollection[0];

    playerPoints = 0;
    
    frameRate(60);
    textFont(flappybirdFont, 100);
}

function draw() { 

    cleanCanvas();

    makePipes();
    for(let i = 0; i < pipeCollection.length; i++) {
        pipeCollection[i].toCanvas();
        pipeCollection[i].scroll(3);
    }

    if (pipeCollection[0].x_coordinate <= 0) {
        hasPipeInQueueForShift = true;
        shiftPipes();
    }

    if (pipeCollection[0].collide(bird)) {
        isPlayerDead = true; // This has no effect yet
    }
    else if (pipeCollection[0].isCleared(bird)) {
        playerPoints += 1;
        scoreboard.buzz();
    }

    scoreboard.toCanvas(playerPoints);

    bird.toCanvas();

    ground.toCanvas();
}


/**
 * Remove all previously drawn elements in the canvas.
 */
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
    return false; /* prevent the browser's default multiple tap action from
                  occuring */
}

/**
 * Create a new pipe set that would serve as an obstacle in the game world.
 */
function makePipes() {
    if ((frameCount % 80 == 0 && !hasPipeInQueueForShift) && 
            (pipeCollection.length != maxNumberOfPipes)) {
        pipeCollection.push(new PipeSet());
    }
}


/**
 * Place the current pipe to the tail of the pipe set collection.
 */
function shiftPipes() {
    /*
        Repurpose the current pipe so that resources won't have to be 
        reloaded for a new pipe set every X number of frames.
    */
    currentPipe.reconstruct();
    pipeCollection.push(currentPipe);
    pipeCollection.shift(); // remove the first pipe set in the pipe set collection
    hasPipeInQueueForShift = false;
    currentPipe = pipeCollection[0];
}

function let_bird_fall() {
    while ((bird.y_coordinate != bird.lowerLimit) || (frameCount % 20 != 0)) {

    }
}