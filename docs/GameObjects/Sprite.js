class Sprite {
    // Represents a 2D image within the game

    // Initializes a new instance of the Sprite class
    // [pathToImage]: The file path to the image that will be 
    // visually representing the sprite
    constructor(pathToImage) {
        this.image = loadImage(pathToImage);
    }
    
    // Draws the image onto the specified canvas or surface
    // [canvas]: The surface wherein the sprite is to be drawn on
    // [location]: The x and y coordinates of the area where the 
    // image is to be drawn on
    // [dimensions]: The desired width and height of the image
    toCanvas(x_coordinate, y_coordinate, transform_height=null, 
        transform_width=null) {
        if (transform_height != null && transform_width !=null) {
            image(this.image, x_coordinate, y_coordinate, 
                transform_width, transform_height);
        }
        else {
            image(this.image, x_coordinate, y_coordinate);
        }
    }


}