// Represents an obstacle in the game
class PipeSet {

    // Initializes a new instance of the PipeSet class
    constructor() {
        this.x_coordinate =  innerWidth;
        this.pipeWidth = 60;
        this.passableSpaceHeight = this.pipeWidth;
        this.offSet = this.pipeWidth / 2;

        this.pipeHead = new Sprite("res/Images/pipe_head.png");
        this.pipeBody = new Sprite("res/Images/pipe_body.png");

        this.topPipeHeight = 0;
        this.bottomPipeHeight = 0;

        this.calculateDimensions();
    }

    // Calculates the height and gap between the two pipes in the pipe set
    calculateDimensions() {
        let maxHeight = Math.abs((innerHeight / 2) - this.passableSpaceHeight * 4);
        // max defines how small the bottom pipe would be since this one grows from top to bottom
        this.bottomPipeHeight = this.getRandom(maxHeight, innerHeight - maxHeight);
        this.topPipeHeight = this.getRandom(this.passableSpaceHeight, maxHeight);        
    }

    // Gradually move the pipe towards the bird and off the screen
    scroll(scrollSpeed=2) {
        this.x_coordinate -= scrollSpeed;
    }

    // Draws the bird onto the specified canvas or surface
    toCanvas() {

        // Pipe head parameters
        let pipeHeadWidth = this.pipeWidth;
        let pipeHeadHeight = this.offSet;

        // Top pipe body parameters
        let topPipeBody_xCoordinate = (this.x_coordinate - this.offSet);
        let topPipeBody_yCoordinate = -this.offSet;
        // Top pipe head paramters
        let topPipeHead_xCoordinate = (this.x_coordinate - this.offSet);
        let topPipeHead_yCoordinate = (this.topPipeHeight - this.offSet);
        // Top pipe dimensions
        let d_topPipeWidth = this.pipeWidth;
        let d_topPipeHeight = this.topPipeHeight;

        // Bottom pipe body parameters
        let bottomPipeBody_xCoordinate = (this.x_coordinate - this.offSet);
        let bottomPipeBody_yCoordinate = this.bottomPipeHeight + this.offSet;
        // Bottom pipe head paramters
        let bottomPipeHead_xCoordinate = (this.x_coordinate - this.offSet);
        let bottomPipeHead_yCoordinate = (this.bottomPipeHeight + this.offSet);
        // Bottom pipe dimensions
        let d_bottomPipeWidth = this.pipeWidth;
        let d_bottomPipeHeight = this.bottomPipeHeight * 4;
        
        // Draw the top pipe
        this.pipeBody.toCanvas(topPipeBody_xCoordinate, topPipeBody_yCoordinate, 
            d_topPipeHeight, d_topPipeWidth);
        this.pipeHead.toCanvas(topPipeHead_xCoordinate, topPipeHead_yCoordinate, 
            pipeHeadHeight, pipeHeadWidth);
        
        // Draw the bottom pipe
        this.pipeBody.toCanvas(bottomPipeBody_xCoordinate, bottomPipeBody_yCoordinate, 
            d_bottomPipeHeight, d_bottomPipeWidth);
        this.pipeHead.toCanvas(bottomPipeHead_xCoordinate, bottomPipeHead_yCoordinate, 
            pipeHeadHeight, pipeHeadWidth);
    }

    /* Determines whether the bird had collided with either of the 
    two pipes in the pipe set
    [bird]: The bird object that the player controls in the game
    [RETURNS]: True if the bird had collided with of any of the pipes
    in the pipe set 
    */
    collide(bird) {
        let bird_in_contact = ((this.x_coordinate - this.pipeWidth) - 
            bird.x_coordinate) <= 0; 
        let midPoint_y = ((this.topPipeHeight + this.bottomPipeHeight) / 2) - 
            this.pipeWidth;
        
        if (
            (bird_in_contact && ((bird.y_coordinate <= this.topPipeHeight) && 
                bird.y_coordinate < midPoint_y)) ||
            (bird_in_contact && ((bird.y_coordinate >= this.bottomPipeHeight) && 
                bird.y_coordinate > midPoint_y))
            ) {
                return true;
            }
            else {
                return false;
            }
    }

    isCleared(bird) {
        let midPoint_x = (this.x_coordinate + bird.x_coordinate) / 2;
        let midPoint_y = (this.topPipeHeight + this.bottomPipeHeight) / 2;

        if (((bird.x_coordinate == midPoint_x) && (bird.y_coordinate >= midPoint_y))
                || ((bird.x_coordinate == midPoint_x) && bird.y_coordinate <= midPoint_y)) {
                return true;
            }
            else {
                return false;
            }
    }

    /*
        Returns a random number between the given intervals min and max
    */
    getRandom(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }
}