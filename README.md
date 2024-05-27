# Rock-Paper-Scissors Game

This is a simple command-line implementation of the classic Rock-Paper-Scissors game in Python. The user can play against the computer until they decide to quit the game. 

## Features

- User vs Computer gameplay.
- Keeps track of the number of wins for both the user and the computer.
- Handles invalid inputs gracefully.
- Allows the user to exit the game by typing `q`.

## How to Run

1. Ensure you have Python installed on your system.
2. Download the `rock_paper_scissors.py` file or clone this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory where the `rock_paper_scissors.py` file is located.
5. Run the script using the command:
   ```sh
   python rock_paper_scissors.py
   ```

## How to Play

1. Run the script.
2. When prompted, type your choice: "Rock", "Paper", or "Scissors".
3. The computer will randomly choose one of the options.
4. The winner of the round will be displayed.
5. The game will keep track of the number of wins for both the user and the computer.
6. To exit the game, type `q`.

## Code Explanation

- **Imports**:
  - `random`: Used to allow the computer to make a random choice.

- **Variables**:
  - `user_wins`: Counter for the number of times the user wins.
  - `computer_wins`: Counter for the number of times the computer wins.
  - `options`: A list of the possible choices (rock, paper, scissors).

- **Game Loop**:
  - The `while True` loop keeps the game running until the user decides to quit.
  - The user's input is taken and converted to lowercase for consistency.
  - If the user types `q`, the loop breaks, ending the game.
  - If the user input is not one of the valid options, a message is printed, and the loop continues.
  - The computer randomly selects one of the options.
  - The winner of each round is determined and the corresponding win counter is incremented.
  - After exiting the loop, the total number of wins for both the user and the computer is displayed.

## Example

```
Type Rock/Paper/Scissors OR q to exit: rock
Computer chose scissors.
You Won!

Type Rock/Paper/Scissors OR q to exit: paper
Computer chose rock.
You Won!

Type Rock/Paper/Scissors OR q to exit: q
You won 2 times.
Computer won 0 times.
Thank you for playing!
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## Contact

If you have any questions, feel free to reach out.

Happy coding!
