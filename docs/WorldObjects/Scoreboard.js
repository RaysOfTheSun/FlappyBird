class Scoreboard {

    constructor() {
        this.xCoordinate = innerWidth / 2;
        this.yCoordinate = innerHeight * 0.125;
        this.offset = 15;        
        this.scoreLength = 0;
        
        this.sound = loadSound("res/sounds/sfx_point.wav");
    }

    toCanvas(score) {
        let newScoreLength = String(score).length;
        if (newScoreLength > this.scoreLength) {
            this.scoreLength = newScoreLength;
            this.xCoordinate -= 15;
        }

        fill(0);
        text(`${score}`, this.xCoordinate, this.yCoordinate + 5);
        fill(255);
        text(`${score}`, this.xCoordinate, this.yCoordinate);
    }

    buzz() {
        this.sound.play();
    }
}