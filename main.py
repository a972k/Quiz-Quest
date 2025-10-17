import json
import threading
import sys
import random
from quiz_quest import get_random_question, open_category

# Start quiz prompt
print("Welcome to the Quiz Quest!")
print("Let's see how much you know.")

# Ask the number of players
num_players = int(input("Enter number of players from 1-5:  "))
while num_players < 1 or num_players > 5:
    num_players = int(input("Invalid input. Please enter a number between 1 and 5: "))
    
# Ask for player names
player_names = []
for i in range(num_players):
    name = input(f"Enter name for player {i + 1}: ")
    player_names.append(name)

# Ask for number of rounds
num_rounds = int(input("Enter number of rounds (1-10): "))
while num_rounds < 1 or num_rounds > 10:
    num_rounds = int(input("Invalid input. Please enter a number between 1 and 10: "))

# Load questions from JSON file

with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

print("Available categories:")
for cat in questions.keys():
    print(f"- {cat}")

# Normalize category keys for case-insensitive matching
category_map = {cat.lower(): cat for cat in questions.keys()}

# 
chosen_category = input("\nChoose a category (or press Enter for random): ").strip().lower()
selected_category = category_map.get(chosen_category) if chosen_category else None

# Shuffle player order
random.shuffle(player_names)

score = {name: 0 for name in player_names}
    
# Shuffle player order
player_order = player_names.copy()
random.shuffle(player_order)
current_player_idx = 0

for round_num in range(num_rounds):
    # Get a random question (from chosen category or all)
    if selected_category:
        question, options, correct_answer = get_random_question(questions, selected_category)
    else:
        question, options, correct_answer = get_random_question(questions)

    print(f"\nRound {round_num + 1}:")
    print(f"Question: {question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")


    answered = False
    # Loop through players until someone answers correctly
    while not answered:
        current_player = player_order[current_player_idx]
        print(f"{current_player}'s turn:")

        # Timer logic
        answer = [None]
        def get_input():
            answer[0] = input("Your answer (15 sec): ").strip()

        t = threading.Thread(target=get_input)
        t.daemon = True
        t.start()
        t.join(timeout=15)

        if t.is_alive():
            print("⏰ Time's up! Next player's turn.")
            # Move to next player for this question
            current_player_idx = (current_player_idx + 1) % len(player_order)
            continue

        user_choice = answer[0]
        if user_choice is None:
            print("No answer received. Next player's turn.")
            current_player_idx = (current_player_idx + 1) % len(player_order)
            continue

        if user_choice.isdigit() and 1 <= int(user_choice) <= len(options):
            user_answer = options[int(user_choice) - 1]
        else:
            user_answer = user_choice

        if user_answer == correct_answer:
            score[current_player] += 1
            print("✅ Correct!")
            print(f"{current_player} scored 1 point!")
            answered = True
            # Move to next player for next question
            current_player_idx = (current_player_idx + 1) % len(player_order)
        else:
            print(f"❌ Wrong. Next player's turn.")
            # Move to next player for this question
            current_player_idx = (current_player_idx + 1) % len(player_order)

    # Display scores after each round
    print("\nCurrent Scores:")
    for player, points in score.items():
        print(f"{player}: {points} points")

    # Display scores after each round
    print("\nCurrent Scores:")
    for player, points in score.items():
        print(f"{player}: {points} points")

# Announce winner
max_score = max(score.values())
winners = [player for player, points in score.items() if points == max_score]
if len(winners) == 1:
    print(f"\n🏆 The winner is {winners[0]} with {max_score} points!")
else:
    print(f"\nIt's a draw between: {', '.join(winners)} with {max_score} points each!")