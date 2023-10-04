# Python Game Library

## Overview

The Game Menu and Scoreboards project is a Python-based application designed to provide a user-friendly menu system for selecting and playing different games, including Flappy Bird, Snake, and Pong. Additionally, it includes scoreboards for each game to track and display the top scores.

## Features

### Game Menu (main.py)

- Run `main.py` to access the game menu.
- The menu allows you to choose from the following games:
  1. Pong
  2. Flappy Bird
  3. Snake
  4. Scores (View game scoreboards)
  5. Quit (Exit the program)

### Game Scoreboards

#### 1. Flappy Bird Scoreboard (fbscoreboard.py)

- This module (`fbscoreboard.py`) provides functionality to display the top 5 scores for the Flappy Bird game.
- The top scores are read from the `fbscores.txt` file in the `games` directory.
- To access the Flappy Bird scoreboard, select "FlappyBird" from the game selector menu.
- Press "ESC" to return to the game selector.

#### 2. Snake Scoreboard (sscoreboard.py)

- This module (`sscoreboard.py`) allows you to view the top 5 scores achieved in the Snake game.
- The highest scores are retrieved from the `sscores.txt` file located in the `games` directory.
- To access the Snake scoreboard, choose "Snake" from the game selector menu.
- Press "ESC" to return to the game selector.

#### 3. Pong Scoreboard (pscoreboard.py)

- The `pscoreboard.py` module is used to display the top 5 scores for the Pong game.
- The high scores are fetched from the `pscores.txt` file in the `games` directory.
- To view the Pong scoreboard, select "Pong" from the game selector menu.
- Press "ESC" to return to the game selector.

### Accessing Scoreboards

- To access any of the scoreboards, select the corresponding game from the game selector menu.
- The top 5 scores for the chosen game will be displayed.
- You can return to the game selector by pressing the "ESC" key.

## Getting Started

1. **Prerequisites**: Ensure that you have Python installed on your system.

2. **Installation**:

   - Clone this repository or download the project files.

3. **Usage**:

   - Run the `main.py` file to access the game menu.
   - Choose a game or the "Scores" option to view scoreboards.
   - Enjoy playing the games and comparing your scores with others!

## Dependencies

This application relies on the following Python modules:

- `pygame`: For game development and graphics rendering.
- `pygame_menu`: For creating the game menu system.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for detailed information.

## Enjoy Your Gaming Experience

Have fun exploring and playing the games provided by the Game Menu and Scoreboards project. Challenge yourself to achieve high scores and aim for the top of the leaderboards! Happy gaming!
