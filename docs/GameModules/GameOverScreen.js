
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

        this.score_xCoordinate = (innerWidth / 2) + 180;
        this.score_yCoordinate = (innerWidth / 2) + 240;
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
        text(String(finalScore), this.score_xCoordinate, this.score_yCoordinate);
    }

    calculateTextY() {
        let yCoordinate = (innerHeight * 0.4876);

        if (innerHeight >= 1750 && innerHeight <= 1760) {
            yCoordinate = (innerHeight * 0.3885); // base: 1757
        }
        else if (innerHeight >= 1900 && innerHeight <= 2000) {
            yCoordinate = (innerHeight * 0.3789); // base: 1979
        }
        else if (innerHeight >= 2100 && innerHeight <= 2240) {
            yCoordinate = (innerHeight * 0.3781); // base: 2142
        }
        else if (innerHeight >= 1317 && innerHeight <= 1377) {
            yCoordinate = (innerHeight * 0.4066); // base: 1377
        }
        else if (innerHeight >= 1580 && innerHeight <= 15600) {
            yCoordinate = (innerHeight * 0.3984) // base: 1581;
        }

        return yCoordinate;
    }
}