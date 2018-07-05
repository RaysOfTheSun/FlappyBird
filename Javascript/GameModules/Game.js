var y = 100;

function setup() {
    // createCanvas must be the first statement
    createCanvas(720, 400);  
    stroke(255);     // Set line drawing color to white
    frameRate(30);
}

function draw() { 
    background(0);   // Set the background to black
    y = y - 1; 
    if (y < 0) { 
      y = height; 
    } 
    line(0, y, width, y);  
  } 