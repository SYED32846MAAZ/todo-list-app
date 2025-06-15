import time
import random

# Sample prompts for the typing test
PROMPTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an interpreted high-level programming language.",
    "Practice makes perfect when learning to type faster.",
    "Coding is fun and typing speed helps you code efficiently."
]

def get_random_prompt():
    """Return a random prompt from the list."""
    return random.choice(PROMPTS)

def calculate_wpm(text, time_sec):
    """Calculate Words Per Minute (WPM)."""
    words = len(text.split())  # Count words typed
    minutes = time_sec / 60
    return round(words / minutes, 2)

def calculate_accuracy(original, typed):
    """Compare original vs. typed text and return accuracy %."""
    correct = sum(o == t for o, t in zip(original, typed))
    return round((correct / len(original)) * 100, 2)

def typing_test():
    """Run the typing speed test."""
    print("===== Typing Speed Test =====")
    prompt = get_random_prompt()
    print(f"\nType this: \"{prompt}\"\n")

    input("Press ENTER to start...")
    start_time = time.time()

    user_input = input("Start typing NOW:\n")
    end_time = time.time()

    time_taken = end_time - start_time
    wpm = calculate_wpm(user_input, time_taken)
    accuracy = calculate_accuracy(prompt, user_input)

    print("\n===== Results =====")
    print(f"Time taken: {round(time_taken, 2)} seconds")
    print(f"Your WPM: {wpm}")
    print(f"Accuracy: {accuracy}%")

if __name__ == "__main__":
    typing_test()
    