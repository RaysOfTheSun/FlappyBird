// The background of the game world
class Backdrop {
    // Initializes a new instance of the Backdrop class
    // [ground_offset]: The offset value of the ground object in the 
    // canvas wherein the backdrop is to be drawn
    constructor(ground_offset) {
        this.offset = ground_offset;
        this.sprite = new Sprite("res/Images/background.png");
        
        this.xCoordinate = 0;
        this.yCoordinate = -this.offset;
    }

    // Draws the backdrop onto the specified canvas or surface 
    toCanvas() {
        this.sprite.toCanvas(this.xCoordinate, this.yCoordinate);
    }
}