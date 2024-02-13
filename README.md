[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=13827628)
# Hangman

Create your own two-player version of the classic word game Hangman.

```text


 __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|

                                      +---+
                                      |   |
                                      O   |
                                     /|\  |
                                     / \  |
                                       =====

```

## Specifications

Your program should:

- Allow one player to enter a secret word for the other player to guess.
- Prompt the player to guess one letter at a time until the player has
  guessed the secret word or run out of guesses.
- After each guess, your program should display the state of the game:
  - the secret word with any correctly guessed letters filled in
  - a list of letters guessed so far
  - the number of guesses remaining
  - ASCII art appropriate to the number of missed guesses
- Display an appropriate message when the player wins or loses.
- When a game has ended, ask the players if they want to play again.
  If so, start a new game. If not, exit the program.

## Plan ahead

Before you write any code, outline the game logic or -- even better --
create a flowchart. **You'll need to submit this outline or flowchart
before you start coding.**

Consider the following:

- What state (data) does your program need to keep track of? What data
  types will you use?
- What steps get repeated? What control structures will you use to
  repeat them? How will your program know when to stop repeating?
- What are the decision points in your program -- steps when your
  program has choose between different actions it could take?
  How will it decide which code path to follow?

## Getting set up

I'll give you a link in class to a GitHub Classroom assignment. Click the
link and accept the assignment. This will create a new repository for you
with a copy of the project files.

Navigate to your repository and launch a Codespace.

## Pseudocode

Translate your outline or flowchart into **pseudocode**.

- Stub out any helper functions
- Try to indent your pseudocode to reflect the structure of your program. For
  example, if you use a loop, indent the pseudocode that explains what you'll do
  in that loop to show that it's part of the loop code block.
- Focus on:
  - What state your program needs to track and how it will be updated
  - Control structures like loops and conditionals

## Craftsmanship

For this project, let's focus on three good programming practices:

- **Descriptive variable names**.
  Use variable names that describe the data they hold.
  For example, `secret_word` is a better variable name than `word` and a much better
  variable name than `w`.
- **Comments**.
  Use precise comments to explain your code when it's helpful, but avoid
  comments where the code explains itself. Function-level comments are generally
  useful and a good place to start.
- **Define single-purpose functions**.
  Rather than lumping all your logic into a
  single function, create smaller functions that have just one job. You might,
  for example, create a function to display the state of the game, another function
  to prompt the player for a guess, and another function to check if the guessed
  letter is in the secret word.

## Submitting your work

`commit` your code and `push` it to your GitHub repository.

## Bonus challenges

Here are a few ideas for extending your program. Have a better idea? Go for it!

- Add a single-player mode. Your game will select a secret word for the player
  to guess. A player should be unlikely to encounter the same secret word twice,
  even after playing many games.
- In two player-mode, keep score. After each game, display the number of games
  won by each player.
- In single-player mode, track a user's win-loss record and current win streak.
  Display win-loss and streak stats after each game.
- Add a difficulty setting. In harder settings, the program should choose longer
  or harder or less common words.
- Allow a user to choose a category from a list of categories. The program should
  select a word appropriate to the category.
