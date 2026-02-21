# 🎮 Memory AI Game - Retro 8-bit Edition

A competitive turn-based memory tile game where you challenge an AI opponent powered by the Minimax algorithm. Built with Flask and featuring a retro 8-bit aesthetic.

---

## 📋 Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [Gameplay Guide](#gameplay-guide)
- [Architecture](#architecture)
- [API Documentation](#api-documentation)
- [Screenshots](#screenshots)
- [Demo Video](#demo-video)
- [File Structure](#file-structure)
- [Team](#team)
- [License](#license)
- [Contributing](#contributing)

---

## 🎯 Project Description

**Memory AI Game** is an interactive web-based game where players compete against an intelligent AI opponent. Players take turns revealing numbered tiles (1-9) on a grid to score points. The challenge lies not in memory, but in strategic decision-making—the AI uses advanced game theory algorithms to calculate optimal moves.

**Key Innovation**: The AI uses **Minimax with Alpha-Beta Pruning** to explore game trees and make unbeatable decisions on Hard difficulty.

### Why This Project?
- Combines game development with artificial intelligence
- Demonstrates algorithmic thinking (game theory)
- Showcases full-stack web development (Flask)
- Fun and challenging gameplay

---

## ✨ Features

1. **Three Difficulty Levels**
   - Easy (AI looks 1 move ahead)
   - Medium (AI looks 3 moves ahead)
   - Hard (AI looks 4-5 moves ahead - nearly unbeatable)

2. **Customizable Grid Sizes**
   - 3×4 (12 tiles)
   - 4×4 (16 tiles - classic)
   - 4×5 (20 tiles)
   - 5×6 (30 tiles - extended)

3. **Intelligent AI Opponent**
   - Uses Minimax algorithm for optimal decision-making
   - Alpha-Beta pruning for performance optimization
   - Adaptive difficulty based on remaining tiles
   - Depth increases to 5 when 6 or fewer tiles remain

4. **Retro 8-bit Aesthetic**
   - Press Start 2P pixel font
   - Neon color scheme (#ff00ff, #00ffcc, #ffff00)
   - Responsive design for mobile/tablet/desktop
   - Sound toggle button

5. **Real-time Score Tracking**
   - Live player vs AI score display
   - Color-coded tiles (green=player, red=AI)
   - Winner announcement modal

6. **Complete Navigation**
   - Home page with rules
   - Difficulty selection
   - Grid size selection
   - Game board with restart option
   - Seamless page linking

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask 3.1.3
- **Language**: Python 3.13
- **WSGI Server**: Gunicorn 25.1.0
- **Environment Management**: python-dotenv 1.2.1

### Frontend
- **Templating**: Jinja2
- **Styling**: CSS3
- **Font**: Google Fonts (Press Start 2P)
- **Client-side Logic**: JavaScript (vanilla)

### AI & Algorithms
- **Game Theory**: Minimax algorithm with Alpha-Beta pruning
- **API Integration**: Google Generative AI (optional)

### Deployment
- **Hosting**: Render.com, Railway.app, or self-hosted
- **Version Control**: Git & GitHub

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/memory-ai-game.git
cd memory-ai-game-main
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create Environment File (Optional)
```bash
# Create .env file in root directory
GEMINI_API_KEY=your_api_key_here  # Optional - game works without it
FLASK_ENV=development
```

---

## 🚀 Running the Game

### Local Development
```bash
# Navigate to project directory
cd memory-ai-game-main

# Run the Flask development server
python app.py
```

**Access the game at**: `http://127.0.0.1:5000`

### Production Deployment (Gunicorn)
```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

### Using Docker (Optional)
```bash
docker build -t memory-ai-game .
docker run -p 5000:5000 memory-ai-game
```

---

## 🎮 Gameplay Guide

### How to Play
1. **Select Difficulty** - Choose from Easy, Medium, or Hard
2. **Select Grid Size** - Pick your preferred grid (3×4, 4×4, 4×5, or 5×6)
3. **Click Tiles** - Reveal numbered tiles to earn points
4. **AI Responds** - The AI automatically picks its best tile
5. **Score Points** - Each tile's number adds to your score
6. **Win Condition** - Highest score when all tiles are revealed wins!

### Scoring System
- Each tile has a number from 1-9
- You earn points equal to the tile's number
- Tiles can only be picked once (they become 0 after)
- Game ends when all tiles are 0

### Difficulty Tips
- **Easy**: Great for learning the game
- **Medium**: Balanced challenge
- **Hard**: AI is nearly unbeatable with optimal play
- **Pro Tip**: Pick high-value tiles early before AI can take them!

---

## 🏗️ Architecture

### System Architecture Diagram
```
┌─────────────────────────────────────────────────────────────┐
│                     User Browser                             │
│  (HTML/CSS/JavaScript - Retro 8-bit UI)                     │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP Requests
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    Flask Server                              │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   Routes    │  │  Game Logic  │  │   Sessions   │       │
│  │ (/game,etc) │  │ (move(), etc)│  │  (board,AI) │       │
│  └─────────────┘  └──────────────┘  └──────────────┘       │
│                       │                                     │
│                       ▼                                     │
│              ┌────────────────────┐                         │
│              │  Minimax Algorithm │                         │
│              │ (AI Decision Tree) │                         │
│              │ Alpha-Beta Pruning │                         │
│              └────────────────────┘                         │
└──────────────────────┬──────────────────────────────────────┘
                       │ Render HTML + Data
                       ▼
┌─────────────────────────────────────────────────────────────┐
│           Jinja2 Templates (Rendering)                       │
│  - index.html (Game Board)                                  │
│  - home.html (Menu)                                         │
│  - grid_select.html (Grid Selection)                        │
└─────────────────────────────────────────────────────────────┘
```

### Game Flow Diagram
```
┌─────────┐
│ START   │
└────┬────┘
     │
     ▼
┌──────────────┐
│ Home Page    │ ◄─────── Select Difficulty (Easy/Medium/Hard)
└────┬─────────┘
     │
     ▼
┌──────────────────┐
│ Grid Selection   │ ◄─── Select Size (3x4, 4x4, 4x5, 5x6)
└────┬─────────────┘
     │
     ▼
┌──────────────────────────────────────┐
│ Initialize Game                      │
│ - Create random board                │
│ - Set scores to 0                    │
│ - Display numbers for 5 seconds      │
└────┬─────────────────────────────────┘
     │
     ▼
┌────────────────────────────────────────────┐
│ Game Loop (Turn-based)                    │
├────────────────────────────────────────────┤
│ 1. Player Clicks Tile                     │
│    ├─ Award player points                 │
│    ├─ Mark tile as revealed               │
│    └─ Check game over?                    │
│                                           │
│ 2. AI Calculates Move (Minimax)           │
│    ├─ Explore game tree (depth-based)     │
│    ├─ Evaluate positions                  │
│    └─ Pick best tile                      │
│                                           │
│ 3. AI Executes Move                       │
│    ├─ Award AI points                     │
│    ├─ Mark tile as revealed               │
│    └─ Check game over?                    │
│                                           │
│ 4. Display Updated Board & Scores         │
└────┬─────────────────────────────────────┘
     │ All tiles revealed?
     ├─ No ──────────────┐
     │                   │
     │                   ▼
     │            (Loop back to Player's turn)
     │
     ├─ Yes ─────────────┐
     │                   │
     ▼                   ▼
┌──────────────────────────────────┐
│ Game Over Modal                  │
│ - Compare Scores                 │
│ - Announce Winner                │
│ - Options: Restart or Back Home  │
└────┬─────────────────────────────┘
     │
     ├─ Restart ────────┐
     │                  │
     │          (New Game Loop)
     │
     ├─ Home ───────────┐
     │                  │
     ▼                  ▼
  [Back to Start]     [Back to Start]
```

### Minimax Algorithm Explanation
```
Minimax(board, depth, isMaximizing):
  If depth = 0 or game over:
    Return evaluation score (AI_score - Player_score)
  
  If Maximizing (AI's turn):
    For each possible tile:
      Score = Minimax(board_after_move, depth-1, False)
      Keep track of best move
    Return best score and move
  
  If Minimizing (Player's turn):
    For each possible tile:
      Score = Minimax(board_after_move, depth-1, True)
      Keep track of best move (lowest for player)
    Return best score and move

Alpha-Beta Pruning:
  - If AI finds a winning move, skip other branches
  - If Player finds a blocking move, skip other branches
  - Result: Faster decisions with same quality
```

---

## 📚 API Documentation

### Flask Routes

#### 1. Home Page
```
GET /
Purpose: Display main menu with difficulty selection
Response: Renders home.html
```

#### 2. Select Grid Size
```
GET /grid/<level>
Parameters:
  - level (str): "easy", "medium", or "hard"
Purpose: Display grid size selection options
Response: Renders grid_select.html
```

#### 3. Start Game
```
GET /start/<level>/<int:grid_rows>/<int:grid_cols>
Parameters:
  - level (str): "easy", "medium", or "hard"
  - grid_rows (int): Number of rows (2-10)
  - grid_cols (int): Number of columns (2-10)
Purpose: Initialize new game with specified parameters
Response: Redirects to /game
```

#### 4. Game Board
```
GET /game
Purpose: Display current game state and board
Response: Renders index.html with game data
Data Passed:
  - original_board: The numbers on each tile
  - player_score: Current player score
  - ai_score: Current AI score
  - revealed: 2D array of revealed tiles
  - owners: Who picked each tile ("player" or "ai")
  - difficulty: Current difficulty level
  - rows, cols: Grid dimensions
  - winner: Winner text (if game over)
```

#### 5. Player Move
```
GET /move/<int:row>/<int:col>
Parameters:
  - row (int): Tile row (0-indexed)
  - col (int): Tile column (0-indexed)
Purpose: Process player tile click and AI response
Process:
  1. Validate move (tile not already picked)
  2. Award points to player
  3. Mark tile as revealed
  4. Call Minimax for AI decision
  5. Execute AI move
  6. Check if game over
Response: Redirects to /game
```

#### 6. Restart Game
```
GET /restart
Purpose: Reset game to initial state with same grid size
Response: Redirects to /game
```

### Session Variables
```python
session = {
    'board': [[0-9, ...], ...],              # Current board state
    'original_board': [[1-9, ...], ...],     # Original numbers
    'player_score': int,                      # Player's total points
    'ai_score': int,                          # AI's total points
    'game_over': bool,                        # Is game finished?
    'difficulty': str,                        # "easy", "medium", "hard"
    'rows': int,                              # Grid height
    'cols': int,                              # Grid width
    'revealed': [[bool, ...], ...],           # Which tiles are picked
    'owners': [[str or None, ...], ...],     # "player", "ai", or None
    'show_numbers': bool                      # Display numbers at start?
}
```

### Error Handling
- Invalid grid dimensions default to 4×4
- Invalid difficulty defaults to "medium"
- Already-picked tiles return 302 redirect (game unchanged)
- Game over state prevents further moves

---

## 🖼️ Screenshots

### Screenshot 1: Home Page
```
<img width="1920" height="1020" alt="Screenshot 2026-02-21 101114" src="https://github.com/user-attachments/assets/a4fbe5dd-32de-4618-b87f-219c92c51c65" />

```

### Screenshot 2: Grid Selection
```
<img width="1920" height="1020" alt="Screenshot 2026-02-21 101131" src="https://github.com/user-attachments/assets/733c4ef3-0225-4000-8785-8250fcba7607" />

```

### Screenshot 3: Gameplay (4×4 Grid)
```
<img width="1920" height="1020" alt="Screenshot 2026-02-21 101200" src="https://github.com/user-attachments/assets/064b0ce0-6a17-4c52-8cdf-af2bce9603fc" />

```

### Screenshot 4: Game Over Modal
```
<img width="1920" height="1020" alt="Screenshot 2026-02-21 101217" src="https://github.com/user-attachments/assets/8260bc75-3e16-44cb-ac0b-dee76319d165" />

```

---

## 🎬 Demo Video

**Demo Video Link**: [(https://docs.google.com/videos/d/1xRza1BHLzJ3f6eHwKZ16wtDJAvVVwFbujiADqm49sCY/edit?usp=drive_link)]
- **Duration**: 2-3 minutes
- **Content**: Full gameplay walkthrough showing:
  1. Menu navigation
  2. Difficulty selection
  3. Grid size selection
  4. Gameplay on Medium difficulty
  5. AI making intelligent moves
  6. Game ending and winner announcement

**Note**: Video will be added in future release

---

## 📁 File Structure

```
memory-ai-game/
│
├── app.py                          # Main Flask application (266 lines)
│   ├── Routes (/, /grid, /start, /game, /move, /restart)
│   ├── Game initialization (new_game)
│   ├── AI Algorithm (minimax, evaluate, is_game_over)
│   └── Difficulty management
│
├── requirements.txt                # Python dependencies
│   ├── flask==3.1.3
│   ├── gunicorn==25.1.0
│   ├── python-dotenv==1.2.1
│   └── google-generativeai==0.8.6
│
├── templates/                      # Jinja2 HTML templates
│   ├── index.html                 # Game board (392 lines)
│   │   ├── Retro 8-bit styling
│   │   ├── Game grid display
│   │   ├── Score tracking
│   │   ├── Winner modal
│   │   └── JavaScript for interactions
│   │
│   ├── home.html                  # Main menu (174 lines)
│   │   ├── Welcome section
│   │   ├── Rules display
│   │   ├── Difficulty buttons
│   │   ├── Sound toggle
│   │   └── Retro styling
│   │
│   └── grid_select.html           # Grid selection (103 lines)
│       ├── Difficulty display
│       ├── Grid size options
│       ├── Back navigation
│       └── Retro styling
│
├── .gitignore                      # Git ignore patterns
│   ├── venv/
│   ├── __pycache__/
│   ├── *.pyc
│   ├── .env
│   └── .DS_Store
│
├── .env (Not in repo)              # Environment variables
│   └── GEMINI_API_KEY
│
├── Procfile                        # Deployment configuration
│   └── web: gunicorn app:app
│
├── README.md                       # This file
├── LICENSE                         # MIT License
└── CHANGELOG.md (Optional)         # Version history
```

### Code Statistics
- **Total Lines**: ~835 lines
- **Backend (app.py)**: 266 lines (AI + routing)
- **Frontend (templates)**: ~669 lines (HTML + CSS + JS)
- **Dependencies**: 4 main packages
- **Routes**: 6 main endpoints

---

## 👥 Team

- **Developer**: Anoushka , Mayoora
  - Backend: Flask, Python, Minimax Algorithm
  - Frontend: HTML, CSS, JavaScript
  - Deployment: Render.com configuration

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

### MIT License Summary
You are free to:
- ✅ Use the project for personal or commercial purposes
- ✅ Modify the code
- ✅ Distribute the code
- ✅ Include in proprietary software

You must:
- ⚠️ Include the original license and copyright notice
- ⚠️ Disclose source code when distributing

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

### Steps to Contribute
1. **Fork the repository**
   ```bash
   Click "Fork" on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/memory-ai-game.git
   cd memory-ai-game-main
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. **Make your changes**
   - Improve AI algorithm
   - Add new grid sizes
   - Enhance UI/styling
   - Add more difficulty levels
   - etc.

5. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```

6. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request**
   - Describe your changes
   - Explain why it's an improvement
   - Reference any issues

### Development Guidelines
- Follow PEP 8 for Python code
- Test locally before submitting PR
- Update documentation if needed
- Keep commits focused and clean

### Suggested Improvements
- [ ] Add multiplayer support
- [ ] Implement different AI strategies
- [ ] Add leaderboard/scoring history
- [ ] Create mobile app version
- [ ] Add sound effects and music
- [ ] Implement undo/replay feature
- [ ] Add bot difficulty settings

---

## 🚀 Deployment Guide

### Deploy to Render.com (Recommended)
https://memory-ai-game-2.onrender.com/game

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Go to Render.com** - https://render.com

3. **Create New Web Service**
   - Connect your GitHub repo
   - Branch: `main`

4. **Configure**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Add `GEMINI_API_KEY` (optional)

5. **Deploy** - Click Deploy and wait 5 minutes

6. **Access** - Your site will be at `https://yourapp.onrender.com`

### Other Deployment Options
- **Railway.app**: Similar to Render, very easy
- **PythonAnywhere**: Python-specific hosting
- **Heroku**: Now requires paid account
- **DigitalOcean**: VPS for $5/month

---

## 📞 Support & Feedback

- **Issues**: Report bugs on GitHub Issues
- **Discussions**: Use GitHub Discussions for questions
- **Email**: contact@example.com (optional)
- **Social Media**: @yoursocialhandle (optional)

---

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Minimax Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Minimax)
- [Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
- [Game Theory Basics](https://www.coursera.org/learn/game-theory-1)

---

## 📊 Project Stats

- ⭐ **Stars**: [Will update after GitHub push]
- 🍴 **Forks**: [Will update after GitHub push]
- 👁️ **Watchers**: [Will update after GitHub push]
- 📦 **Releases**: 1.0.0
- 📝 **Last Updated**: February 21, 2026

---

## 🎉 Acknowledgments

- **Font**: Press Start 2P from Google Fonts
- **Inspiration**: Classic memory games and AI algorithms
- **Framework**: Flask team for the excellent framework
- **Community**: Thanks to all contributors and testers

---

<div align="center">

### Made with ❤️ and Python

[🎮 Play Game](#-running-the-game) • [📖 Read Docs](#-api-documentation) • [🐛 Report Bug](https://github.com/yourusername/memory-ai-game/issues) • [💡 Suggest Feature](https://github.com/yourusername/memory-ai-game/discussions)

</div>

---

**Last Updated**: February 21, 2026  
**Version**: 1.0.0  
**Status**: ✅ Stable & Playable
