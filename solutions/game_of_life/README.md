# Game Of Life with Tkinter in Python

This is a simple implementation of Conway's Game of Life using Python and
Tkinter. It creates a grid-based simulation where cells live, die, or are
born based on simple rules.

![Game of Life Screenshot](https://i.imgur.com/GLKGYnW.png)

## How it Works

- **Grid**: The game runs on a grid of cells.
- **Rules**:
  - A live cell with fewer than 2 or more than 3 neighbors dies.
  - A dead cell with exactly 3 neighbors becomes alive.
- **Controls**:
  - **Pause/Resume**: Toggle the simulation.
  - **Step**: Advance the simulation one generation at a time.
  - **Quit**: Exit the game.

The game is seeded with random live cells when it starts.

---

## How to Run

1. **Clone or download the project.**
2. **Run the game**:

   ```bash
   python game_of_life.py
   ```

---

## Running Tests

A test file is included to ensure the rules are applied correctly.

To run the tests, use:

```bash
python -m unittest test_game_of_life.py
```
