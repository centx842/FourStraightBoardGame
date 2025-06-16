# Tic-Tac-Toe Reimagined

Welcome to the exciting world of Tic-Tac-Toe Reimagined — a fresh and engaging twist on the classic game you know and love! This isn’t your ordinary tic-tac-toe; instead of the traditional 3x3 grid, get ready to challenge your strategic skills on a spacious 6x6 board. The objective? Align four of your marks in a row — horizontally, vertically, or diagonally — to claim victory and outsmart your opponent.

To add even more variety and customization to your gameplay experience, the board size is flexible! You can choose to play on a 5x5, 6x6, or even a massive 10x10 grid. Each board size brings its own unique challenges and strategies, allowing you to tailor the game to your preferred level of complexity and excitement. Whether you want a quick, intense match or a longer, more strategic battle, the choice is yours.

Whether you’re a solo player craving a worthy challenge or looking to enjoy a friendly duel, this game has you covered. You can test your wits against an intelligent PPO (Proximal Policy Optimization) Agent, designed to learn and adapt, offering a dynamic and thrilling gameplay experience. Or, if you prefer the classic human rivalry, invite a friend and battle head-to-head in a race of quick thinking and tactical moves.

To keep the pace lively and add an extra layer of excitement, each turn is timed. This timer ensures that every decision counts, pushing players to think fast and act decisively. No more stalling or endless pondering — just pure, fast-paced fun!

Track your progress and bragging rights with the built-in scoreboard, which keeps a running tally of games won by each player or the AI agent. Whether you dominate the leaderboard or engage in friendly competition, the scoreboard adds a competitive edge that keeps you coming back for more.

Dive into this modern take on a timeless game and experience the perfect blend of strategy, speed, and smart AI competition. Get ready to make your mark on the 6x6 grid and prove who truly masters the art of four in a row!


---

## Getting Started

1. Clone the repository:

   ```bash
   git clone git@github.com:centx842/FourStraightBoardGame.git
   cd FourStraightBoardGame
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash#Getting Started:

git clone git@github.com:centx842/FourStraightBoardGame.git

cd FourStraightBoardGame

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

export PYTHONPATH=$PYTHONPATH:/home/jahangir/projects/FourStraightBoardGame


## Testing:

pytest tests/test_tictactoe.py


4. Set the `PYTHONPATH` environment variable:

   ```bash
   export PYTHONPATH="$PYTHONPATH:/home/jahangir/projects/FourStraightBoardGame"
   ```

---

## Running Application

```bash
python Resources/TicTacToe_Agent.py
```

---


## Running Tests

Execute the test suite using `pytest`:

```bash
pytest tests/test_tictactoe.py
```

