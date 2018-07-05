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

        this.birdWidth = 40;

        this.upperLimit = height / this.birdWidth
        this.lowerLimit = (height - this.birdWidth) - this.ground_offset
        this.sprites = new Sprite("res/Images/bird_wing_down.png")
    }

    toCanvas() {
        this.sprites.toCanvas(this.x_coordinate, this.y_coordinate)
    }



}