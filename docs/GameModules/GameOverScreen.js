
/**
 * Represents the game's game over screen
 * @class GameOverScreen
 */
class GameOverScreen {

    /**
     * Creates an instance of GameOverScreen.
     * @memberof GameOverScreen
     */
    constructor() {
        this.bronzeMedal = new Sprite("res/Images/bronze.png");
        this.goldMedal = new Sprite("res/Images/gold.png");
        this.platinumMedal = new Sprite("res/Images/platinum.png");
        
        this.title = new Sprite("res/Images/gameOver.png");
        this.board = new Sprite("res/Images/game_over_board.png");

        this.title_xCoordinate = (innerWidth * 0.3);
        this.title_yCoordinate = (innerHeight * 0.2179);

        this.board_xCoordinate = (innerWidth / 4) + 20;
        this.board_yCoordinate = (innerWidth / 2) + 120;

        this.score_xCoordinate = ((innerWidth / 2) + 190);
        this.score_yCoordinate = (innerWidth / 2) + 235;

        this.scoreLength = 0;
        this.offset = 0;
    }

    /**
     * Display the game over screen along with the player's final score.
     * @param {Number} finalScore The player's final score.
     * @memberof GameOverScreen
     */
    play(finalScore) {
        textSize(50);
        this.board.toCanvas(this.board_xCoordinate, this.board_yCoordinate);
        this.title.toCanvas(this.title_xCoordinate, this.title_yCoordinate);
        this.scoreTextToCanvas(finalScore);
    }

    /**
     * Render the player's score onto the canvas.
     * @param {Number} finalScore The player's final score.
     * @memberof GameOverScreen
     */
    scoreTextToCanvas(finalScore) {
        if (this.offset == 0) {
            this.offset = this.calculateTextOffset(finalScore);
        }

        fill(0);
        text(String(finalScore), this.score_xCoordinate - this.offset, 
        this.score_yCoordinate + 5);
        fill(255);
        text(String(finalScore), this.score_xCoordinate - this.offset, 
                this.score_yCoordinate);
    }

    /**
     * Determines the space to be applied to the score text's x-coordinate.
     * @param {Number} finalScore The player's final score.
     * @returns A Number that represents the value of the offset
     * @memberof GameOverScreen
     */
    calculateTextOffset(finalScore) {
        
        let scoreStrLength = String(finalScore).length;
        if (this.scoreLength < scoreStrLength) {
            this.scoreLength = scoreStrLength;
        }

        let offset = 0;

        if (this.scoreLength == 2) {
            offset = 10;
        }
        else if (this.scoreLength == 3) {
            offset = 40;
        }
        else if (this.scoreLength == 4) {
            offset = 60;
        }

        return offset;
    }
}