class Bird {
    // Represents the characteristics and functionalities of a bird
    // in the game

    // Initializes a new instance of the Bird class
    // [ground_offset]: The The distance from the bottom of the canvas 
    // to the top of the ground in the game world
    // [y_coordinate]: The position of the bird on the y-axis
    // [x_coordinate]: The position of the bird on the x-axis
    constructor(ground_offset, y_coordinate, x_coordinate = 60) {
        this.ground_offset = ground_offset;
        this.x_coordinate = x_coordinate;
        this.y_coordinate = y_coordinate;

        this.birdWidth = 40; // Determines the height and width of the bird
        this.pull = -14; // application will result into negative velocity
        this.gravity = 1; // the force the pulls the bird downward
        this.velocity = -2; // dictates the speed and direction of the bird

        // The bird should now go over the upper and lower bounds of the canvas
        this.upperLimit = height / this.birdWidth;
        this.lowerLimit = (height - this.birdWidth) - this.ground_offset;

        this.sprites = new Sprite("res/Images/bird_wing_down.png");
        this.jumped = false;
    }

    // Draws the bird onto the specified canvas or surface
    // [canvas]: The surface wherein the bird is to be drawn on
    toCanvas() {

        if (this.jumped) {
            this.fly();
        }
        else {
            this.fall();
        }

        this.updatePosition();

        this.sprites.toCanvas(this.x_coordinate, this.y_coordinate, 
            this.birdWidth, this.birdWidth);
    }

    fall() {
        if (this.y_coordinate != this.lowerLimit) {
            this.velocity += this.gravity;
            this.pull = -14;
        }
    }

    fly() {
        if (this.y_coordinate > this.upperLimit) { 
            this.pull += 2;
            this.velocity += this.pull;
        }

        this.jumped = false;
    }

    updatePosition() {
        if ((this.y_coordinate <= 1) && (!this.jumped)) {
            this.y_coordinate = this.upperLimit;
            this.velocity = 0;
        }
        else if ((this.y_coordinate >= (height - this.ground_offset))) {
            this.y_coordinate = this.lowerLimit;
            this.velocity = 0;
        }
        else {
            this.y_coordinate += this.velocity;
        }
    }

    jump() {
        this.jumped = true;
    }

    reset() {
        this.x_coordinate = 60;
        this.y_coordinate = height / 2;
    }



}