# Importing necessary libraries
from flask import Flask, render_template, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Initialize the game state
game_state = {
    # The game board represented as a list of 9 empty strings
    "board": ["" for _ in range(9)],
    # The current player, starting with "X"
    "current_player": "X",
    # Winner of the game (None if no winner yet)
    "winner": None
}

# Define the route for the home page
@app.route("/")
def index():
    # Render the index.html template and pass the game state variables
    return render_template("index.html", board=game_state["board"], current_player=game_state["current_player"], winner=game_state["winner"])

# Define the route for making a move
@app.route("/make_move", methods=["POST"])
def make_move():
    global game_state  # Access the global game state
    data = request.get_json()  # Get the JSON data from the request
    cell_index = data.get("cell_index")  # Get the cell index from the request data

    # Check if the move is invalid (game already won or cell occupied)
    if game_state["winner"] or game_state["board"][cell_index]:
        return jsonify({"error": "Invalid move"})  # Return an error response

    # Make the move by setting the cell to the current player's symbol
    game_state["board"][cell_index] = game_state["current_player"]

    # Check if the move resulted in a win or draw
    winner = check_winner()
    if winner:
        game_state["winner"] = winner  # Update the winner in the game state
    else:
        # Switch the current player
        game_state["current_player"] = "O" if game_state["current_player"] == "X" else "X"

    # Return the updated game state as JSON
    return jsonify({"board": game_state["board"], "current_player": game_state["current_player"], "winner": game_state["winner"]})

# Function to check if there is a winner or a draw
def check_winner():
    board = game_state["board"]  # Get the current game board
    # Define all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    # Check each winning combination
    for combo in winning_combinations:
        # Check if all cells in the combination are the same and not empty
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]]:
            return board[combo[0]]  # Return the winner symbol ("X" or "O")

    # Check if all cells are filled (draw)
    if all(cell for cell in board):
        return "Draw"  # Return "Draw" if no cells are empty

    return None  # Return None if no winner or draw

# Define the route for resetting the game
@app.route("/reset", methods=["POST"])
def reset():
    global game_state  # Access the global game state
    # Reset the game state to its initial values
    game_state = {
        "board": ["" for _ in range(9)],
        "current_player": "X",
        "winner": None
    }
    # Return the reset game state as JSON
    return jsonify({"board": game_state["board"], "current_player": game_state["current_player"], "winner": game_state["winner"]})

# Run the application if the script is executed directly
if __name__ == "__main__":
    app.run('0.0.0.0',8080)
