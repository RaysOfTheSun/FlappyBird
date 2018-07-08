
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

        this.offset = 0;
        this.highScoreOffset = 0;
    }

    /**
     * Display the game over screen along with the player's final score.
     * @param {Number} finalScore The player's final score.
     * @memberof GameOverScreen
     */
    play(finalScore) {
        this.recordScore(finalScore);

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

        this.calculateOffsets(finalScore);
        let highScore = this.getHighScore();

        fill(0);
        text(String(finalScore), this.score_xCoordinate - this.offset, 
        this.score_yCoordinate + 5);
        fill(255);
        text(String(finalScore), this.score_xCoordinate - this.offset, 
                this.score_yCoordinate);

        fill(0);
        text(String(highScore), this.score_xCoordinate - this.highScoreOffset, 
        this.score_yCoordinate + 95);
        fill(255);
        text(String(highScore), this.score_xCoordinate - this.highScoreOffset, 
                this.score_yCoordinate + 90);
    }

    /**
     * Determines the space to be applied to the score text's x-coordinate.
     * @param {Number} finalScore The player's final score.
     * @returns A Number that represents the value of the offset
     * @memberof GameOverScreen
     */
    calculateTextOffset(finalScore) {
        
        let scoreStrLength = String(finalScore).length;

        let offset = 0;

        if (scoreStrLength == 2) {
            offset = 10;
        }
        else if (scoreStrLength == 3) {
            offset = 40;
        }
        else if (scoreStrLength == 4) {
            offset = 60;
        }

        return offset;
    }

    /**
     * Initializes the variables used by the object to determine alignmnet of
     * score strings.
     * @param {Number} finalScore The player's final score.
     * @memberof GameOverScreen
     */
    calculateOffsets(finalScore) {
        if(this.offset == 0 && this.highScoreOffset == 0) {
            this.offset = this.calculateTextOffset(finalScore);
            this.highScoreOffset = this.calculateTextOffset(this.getHighScore());
        }
    }

    /**
     * Save the player's high score to a cookie
     * @param {Number} finalScore The player's final score.
     * @memberof GameOverScreen
     */
    recordScore(finalScore) {
        if (this.getHighScore() < finalScore) {
            docCookies.setItem("score", finalScore);
        }
    }

    /**
     * Retrieve the player's current high score.
     * @returns A number representing the player's high score if it is available.
     * 0 (zero) is returned otherwise.
     * @memberof GameOverScreen
     */
    getHighScore() {
        if (docCookies.getItem("score") != null) {
            return docCookies.getItem("score"); 
        }

        return 0;
    }

    /**
     * Reinitializes the variables that is used by the object to determine alignment
     * of score strings.
     * @memberof GameOverScreen
     */
    reset() {
        this.offset = 0;
        this.highScoreOffset = 0;
    }
}