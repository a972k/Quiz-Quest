# Quiz Quest

Quiz Quest is a multiplayer quiz game played in the terminal. Players compete to answer questions from various categories, with each question passed to the next player if not answered correctly or within the time limit. The game tracks scores and announces the winner at the end.

## Gameplay

- Choose the number of players (1-5) and enter each player's name.
- Select the number of rounds (1-10).
- Pick a category (Science, History, Pop Culture) or let the game choose randomly.
- Players are shuffled into a random order.
- For each round, a question is asked to the current player:
  - The player has 15 seconds to answer.
  - If the answer is wrong or time runs out, the question passes to the next player.
  - The question continues to rotate until someone answers correctly and scores a point.
  - The next question starts with the next player in line.
- Scores are displayed after each round.
- At the end, the player(s) with the highest score win. If there is a tie, all top scorers are announced as winners.

## Technical Background

- The game is written in Python and runs in the terminal.
- Questions are loaded from a JSON file (`questions.json`) organized by category.
- The main game logic is in `main.py`, which handles user input, timing, scoring, and player rotation.
- A 15-second timer for each answer is implemented using Python's `threading` module.
- The game uses randomization for player order and question selection.
- The code is modular, with helper functions in `quiz_quest.py` for question handling.

## Requirements

- Python 3.7 or higher

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/a972k/Quiz-Quest.git
   ```
2. Navigate to the project folder:
   ```
   cd Quiz-Quest
   ```
3. Run the game:
   ```
   python main.py
   ```

## Customization

- You can add or edit questions in `questions.json`.
- Categories can be expanded by adding new keys and question lists in the JSON file.

## License

This project is open source and available under the MIT License.
