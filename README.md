# Tic-Tac-Toe Reimagined

**Tic-Tac-Toe Reimagined** offers a modern and strategic evolution of the classic game. Moving beyond the traditional 3x3 format, this version challenges players on a more expansive 6x6 grid, where the objective is to align four of your marks — horizontally, vertically, or diagonally — to achieve victory.

To enhance the gameplay experience, the board size is configurable. Choose between 5x5, 6x6, or an extensive 10x10 grid to match your preferred level of difficulty and game duration. Each configuration introduces new dynamics and strategic considerations, ensuring a fresh challenge every time you play.

This game supports both single-player and two-player modes. Compete against a friend in head-to-head gameplay, or test your strategy against an intelligent PPO (Proximal Policy Optimization) Agent. The AI adapts and learns from experience, providing a stimulating and unpredictable opponent.

To maintain a fast-paced environment, each move is time-bound. The built-in turn timer encourages swift decision-making, eliminating delays and promoting an engaging, energetic flow of play.

A scoreboard tracks victories for both human players and the AI agent, adding a competitive element and motivating continuous improvement. Whether you're aiming to climb the leaderboard or simply enjoy a casual match, Tic-Tac-Toe Reimagined delivers a compelling mix of strategy, speed, and skill.

Embrace this innovative twist on a timeless favorite and prove your mastery in the game of four in a row.

---

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone git@github.com:centx842/FourStraightBoardGame.git
   cd FourStraightBoardGame
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set the `PYTHONPATH`**:

   Update your environment variable to include the project directory:

   ```bash
   export PYTHONPATH="$PYTHONPATH:/home/jahangir/projects/FourStraightBoardGame"
   ```

---

## Running the Application

Execute the main game loop:

```bash
python Resources/TicTacToe_Agent.py
```

---

## Running Tests

Use `pytest` to run the test suite:

```bash
pytest tests/test_tictactoe.py
```

---
