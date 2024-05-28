from pathlib import Path
import json
import random

def print_random_card(cards):
    headings = list(cards.keys())
    heading = random.choice(headings)
    content = cards[heading]
    print(f"Your flashcard is:\n\t\t\t\t\t{heading}\n\n{content}\n")

def flashcards(cards):
    for key, value in cards.items():
        print(f"\n{key}:\t{value}")

def add_card(cards):
    card_heading = input("Enter the flashcard heading: ")
    card_content = input("Enter the content of the flashcard: ")
    cards[card_heading] = card_content
    update(cards)
    print("The flashcard has been added successfully.")

def remove(cards, key):
    if key in cards:
        del cards[key]
        print(f"The flashcard with the heading {key} has been successfully deleted.")
        update(cards)
    else:
        print(f"Heading '{key}' is not found in the flashcards.")

def print_commands():
    path = Path("commands.txt")
    available_commands = path.read_text(encoding='utf-8')
    print(available_commands)

def extract():
    path = Path("cards.json")
    raw_content = path.read_text()
    content = json.loads(raw_content)
    return content

def update(information):
    path = Path("cards.json")
    content = json.dumps(information)
    path.write_text(content)

def ask():
    mes = input("Enter your command: ")
    ans = mes.lower()
    cards = extract()

    if ans == "view":
        flashcards(cards)
    
    if ans == "random":
        print_random_card(cards)

    if ans == "add":
        add_card(cards)

    if ans == "remove":
        for key, value in cards.items():
            print(f"{key}:\t{value}")
        heading = input("Enter the heading of the flashcard you want to delete: ")
        remove(cards, heading)

    if ans == "help":
        print_commands()

    if not ans == "exit":
        loopin()
    else:
        print("Good bye...")

def loopin():
    try:
        ask()
    except KeyboardInterrupt:
        print("Good bye...")

print_commands()

try:
    ask()
except KeyboardInterrupt:
    print("Good bye...")