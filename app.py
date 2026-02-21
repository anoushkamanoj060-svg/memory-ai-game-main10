from flask import Flask, render_template, redirect, url_for, session
import random
import math
import copy
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
GEMINI_API_KEY = "AIzaSyBPxkfnBlNXfQIFXew8wi4O7v51P257zLc"

# Initialize Gemini API
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("Warning: GEMINI_API_KEY not found in .env file")
app = Flask(__name__)
app.secret_key = "super_secret_key_change_this"

DEFAULT_ROWS, DEFAULT_COLS = 4, 4

# -------------------------
# Game Initialization
# -------------------------
def new_game(rows=DEFAULT_ROWS, cols=DEFAULT_COLS):
    board = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
    session['board'] = board
    session['original_board'] = copy.deepcopy(board)
    session['player_score'] = 0
    session['ai_score'] = 0
    session['game_over'] = False
    session['difficulty'] = "medium"
    session['rows'] = rows
    session['cols'] = cols
    session['revealed'] = [[False for _ in range(cols)] for _ in range(rows)]
    session['owners'] = [[None for _ in range(cols)] for _ in range(rows)]
    session['show_numbers'] = True


# -------------------------
# Check if game is over
# -------------------------
def is_game_over(board):
    return all(val == 0 for row in board for val in row)


# -------------------------
# Evaluation
# -------------------------
def evaluate(ai_score, player_score):
    return ai_score - player_score


# -------------------------
# Minimax with Alpha-Beta
# -------------------------
def minimax(board, depth, maximizing, ai_score, player_score, alpha, beta):
    rows = len(board)
    cols = len(board[0]) if board else 0

    if depth == 0 or is_game_over(board):
        return evaluate(ai_score, player_score), None

    best_move = None

    if maximizing:
        max_eval = -math.inf

        for i in range(rows):
            for j in range(cols):
                if board[i][j] != 0:
                    temp = board[i][j]
                    board[i][j] = 0

                    eval_score, _ = minimax(
                        board, depth - 1, False,
                        ai_score + temp, player_score,
                        alpha, beta
                    )

                    board[i][j] = temp

                    if eval_score > max_eval:
                        max_eval = eval_score
                        best_move = (i, j)

                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        return max_eval, best_move

        return max_eval, best_move

    else:
        min_eval = math.inf

        for i in range(rows):
            for j in range(cols):
                if board[i][j] != 0:
                    temp = board[i][j]
                    board[i][j] = 0

                    eval_score, _ = minimax(
                        board, depth - 1, True,
                        ai_score, player_score + temp,
                        alpha, beta
                    )

                    board[i][j] = temp

                    if eval_score < min_eval:
                        min_eval = eval_score
                        best_move = (i, j)

                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        return min_eval, best_move

        return min_eval, best_move


# -------------------------
# Home Page
# -------------------------
@app.route('/')
def home():
    return render_template('home.html')


# -------------------------
# Grid Selection
# -------------------------
@app.route('/grid/<level>')
def select_grid(level):
    if level in ["easy", "medium", "hard"]:
        session['difficulty'] = level
    return render_template('grid_select.html', difficulty=level)

# -------------------------
# Start Game with Grid
# -------------------------
@app.route('/start/<level>/<int:grid_rows>/<int:grid_cols>')
def start_game_with_grid(level, grid_rows, grid_cols):
    if level in ["easy", "medium", "hard"]:
        session['difficulty'] = level
    if 2 <= grid_rows <= 10 and 2 <= grid_cols <= 10:
        new_game(rows=grid_rows, cols=grid_cols)
    else:
        new_game()
    return redirect(url_for('index'))


# -------------------------
# Game Page
# -------------------------
@app.route('/game')
def index():

    if 'board' not in session:
        new_game()

    winner = None

    if session['game_over']:
        if session['player_score'] > session['ai_score']:
            winner = "Player Wins!"
        elif session['ai_score'] > session['player_score']:
            winner = "AI Wins!"
        else:
            winner = "Draw!"

    return render_template(
        'index.html',
        original_board=session['original_board'],
        player_score=session['player_score'],
        ai_score=session['ai_score'],
        game_over=session['game_over'],
        show_numbers=session['show_numbers'],
        revealed=session['revealed'],
        owners=session['owners'],
        difficulty=session['difficulty'],
        rows=session.get('rows', DEFAULT_ROWS),
        cols=session.get('cols', DEFAULT_COLS),
        winner=winner
    )


# -------------------------
# Player Move
# -------------------------
@app.route('/move/<int:row>/<int:col>')
def move(row, col):

    board = session['board']
    revealed = session['revealed']
    owners = session['owners']

    if board[row][col] == 0 or session['game_over']:
        return redirect(url_for('index'))

    session['show_numbers'] = False

    # Player move
    session['player_score'] += board[row][col]
    revealed[row][col] = True
    owners[row][col] = "player"
    board[row][col] = 0

    if is_game_over(board):
        session['game_over'] = True
        session.modified = True
        return redirect(url_for('index'))

    # Difficulty Depth
    depth_map = {
        "easy": 1,
        "medium": 3,
        "hard": 4
    }

    remaining = sum(val != 0 for row in board for val in row)

    if remaining <= 6:
        ai_depth = 5
    else:
        ai_depth = depth_map.get(session['difficulty'], 3)

    _, best_move = minimax(
        copy.deepcopy(board),
        ai_depth,
        True,
        session['ai_score'],
        session['player_score'],
        -math.inf,
        math.inf
    )

    if best_move:
        i, j = best_move
        session['ai_score'] += board[i][j]
        revealed[i][j] = True
        owners[i][j] = "ai"
        board[i][j] = 0

    if is_game_over(board):
        session['game_over'] = True

    session['board'] = board
    session['revealed'] = revealed
    session['owners'] = owners
    session.modified = True

    return redirect(url_for('index'))


# -------------------------
# Restart
# -------------------------
@app.route('/restart')
def restart():
    new_game()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)