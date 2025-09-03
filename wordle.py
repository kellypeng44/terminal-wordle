import random

def load_words(filename):
    with open(filename, "r") as f:
        return [w.strip().lower() for w in f if len(w.strip()) == 5]
    
# Load word lists
ANSWER_LIST = load_words("./wordle-answers-alphabetical.txt")
GUESS_LIST = load_words("./words.txt")

def pick_word(word_list):
    return random.choice(word_list)

def check_guess(guess, answer):
    result = []
    for i, letter in enumerate(guess):
        if letter == answer[i]:
            result.append("🟩")  # in the word & correct spot
        elif letter in answer:
            result.append("🟨")  # in the word but wrong spot
        else:
            result.append("⬜")  # not in the word
    return "".join(result)

def play_wordle():
    answer = pick_word(ANSWER_LIST)
    attempts = 6

    print("Guess the Wordle in 6 tries. \n")

    while attempts > 0:
        guess = input(f"Attempt {attempts}/6: ").lower()

        if len(guess) != 5:
            print("❌ Invalid guess. Must be 5 letters.")
            continue
        # check if the guess is in the allowed guess list
        if guess not in GUESS_LIST: 
            print("❌ Invalid guess. Must be a valid word.")
            continue

        feedback = check_guess(guess, answer)
        print(feedback)
        
        attempts -= 1

        if guess == answer:
            print("\n You win! 🎉")
            break
    else:
        print(f"Out of tries😢 The word was: {answer}")

if __name__ == "__main__":
    play_wordle()