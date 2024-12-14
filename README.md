
# Tic Tac Toe Game-2 with Flask

This project implements a simple Tic Tac Toe game using Python Flask for the backend and HTML for the frontend. Players can take turns to make moves on a 3x3 grid, and the application checks for winners or a draw.

## Features

-   Interactive Tic Tac Toe game.
    
-   Player turn management.
    
-   Automatic winner or draw detection.
    
-   Reset functionality to restart the game.
    

## Prerequisites

-   Python 3.x
    
-   Flask (Install using `pip install flask`)
    

## Installation

1.  Clone this repository or download the files.
    
2.  Navigate to the project directory.
    
3.  Install Flask:
    
    ```
    pip install flask
    ```
    

## File Structure

```
project/
├── app.py               # Flask backend for the game
├── templates/
│   └── index.html       # Frontend HTML template
```

## Usage

1.  Run the Flask application:
    
    ```
    python app.py
    ```
    
2.  Open your browser and navigate to:
    
    ```
    http://127.0.0.1:5000/
    ```
    
3.  Play the game by clicking on the grid cells. The current player's turn is displayed.
    
4.  Reset the game by clicking the "Reset Game" button.
    

## API Endpoints

### `POST /make_move`

-   **Description**: Makes a move for the current player.
    
-   **Request Data**: JSON object with the `cell_index` (0-8) of the grid.
    
-   **Response Data**: JSON object with the updated `board`, `current_player`, and `winner`.
    

### `POST /reset`

-   **Description**: Resets the game state.
    
-   **Response Data**: JSON object with the initial game state.
    

## Game Rules

1.  The game is played on a 3x3 grid.
    
2.  Players take turns to place their marker (`X` or `O`) in an empty cell.
    
3.  The first player to align three markers horizontally, vertically, or diagonally wins.
    
4.  If all cells are filled and no player wins, the game ends in a draw.
    

## Screenshots
![Front end](https://github.com/sugeng-riyanto/Tic-Tac-Toe-game-using-flask-python/blob/main/Tic-Tac-Toe-12-14-2024_05_50_PM.png)

## License

This project is licensed under the MIT License.
