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

        this.birdWidth = 55; // Determines the height and width of the bird
        this.pull = -14; // application will result into negative velocity
        this.gravity = 1; // the force the pulls the bird downward
        this.velocity = -2; // dictates the speed and direction of the bird

        // The bird should now go over the upper and lower bounds of the canvas
        this.upperLimit = innerHeight / this.birdWidth;
        this.lowerLimit = (innerHeight - this.birdWidth) - this.ground_offset;

        this.sprites = new Sprite("res/Images/bird_wing_down.png");
        this.flapSound = loadSound("res/sounds/sfx_wing_flap.wav");
        this.jumped = false;
    }

    // Draws the bird onto the specified canvas or surface
    toCanvas() {

        if (this.jumped) {
            this.fly();
        }
        else {
            this.fall();
        }

        this.updatePosition();

        this.sprites.toCanvas(this.x_coordinate, this.y_coordinate);
    }

    // Pushes the bird downward
    fall() {
        if (this.y_coordinate != this.lowerLimit) {
            this.velocity += this.gravity;
            this.pull = -14;
        }
    }
    // Pushes the bird upward
    fly() {
        if (this.y_coordinate > this.upperLimit) { 
            this.pull += 2;
            this.velocity += this.pull;
            this.flapSound.play();
        }

        this.jumped = false;
    }

    // Updates the position of the bird and also restricts it to within 
    // the visible area of the canvas
    updatePosition() {
        if ((this.y_coordinate <= 1) && (!this.jumped)) {
            this.y_coordinate = this.upperLimit;
            this.velocity = 0;
        }
        else if ((this.y_coordinate >= (innerHeight - this.ground_offset))) {
            this.y_coordinate = this.lowerLimit;
            this.velocity = 0;
        }
        else {
            this.y_coordinate += this.velocity;
        }
    }

    // Activate the bird object's flight mechanism
    jump() {
        this.jumped = true;
    }

    // Puts the bird back to its initial location
    reset() {
        this.x_coordinate = 60;
        this.y_coordinate = innerHeight / 2;
    }
}