# Quiz Game

This is a Python-based quiz game that fetches trivia questions from the Open Trivia Database (OpenTDB). Players can choose from various categories, difficulty levels, and question types. The game will then fetch the selected number of questions and present them to the player, who will answer and receive a score based on their performance.

## Features

- **Categories**: The game fetches a list of trivia categories from the [OpenTDB API](https://opentdb.com/api_config.php), allowing players to choose their preferred category.
- **Difficulty Levels**: Players can choose from three difficulty levels: Easy, Medium, and Hard.
- **Question Types**: The game supports two types of questions: Multiple Choice and True/False.
- **Score Calculation**: The game keeps track of the player's score and displays it at the end.

## How It Works

1. **Fetching Categories**: The game fetches available categories from the [OpenTDB API](https://opentdb.com/api_config.php) and displays them to the player.
2. **Choosing a Category**: Players select a category by inputting the category ID.
3. **Choosing Difficulty and Question Type**: Players select the difficulty level and question type.
4. **Fetching Questions**: The game fetches questions based on the selected category, difficulty level, and question type.
5. **Answering Questions**: Players answer the questions presented, and the game tracks their score.
6. **Displaying Score**: At the end of the quiz, the game displays the player's score.

## Requirements

- Python 3.x
- `requests` library (install with `pip install requests`)

## Usage

1. **Run the Game**: Execute the script to start the game.
2. **Follow Prompts**: The game will prompt you to select a category, difficulty level, question type, and the number of questions.
3. **Answer Questions**: Input your answers as prompted.
4. **View Score**: At the end of the quiz, your score will be displayed.

## API Information

The game uses the [OpenTDB API](https://opentdb.com/api_config.php) to fetch trivia questions.

**Categories**: https://opentdb.com/api_category.php.
**Questions**: https://opentdb.com/api.php?amount={num_ques}&category={category_id}&difficulty={diff_level}&type={ques_type}
