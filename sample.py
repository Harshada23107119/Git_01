import random

QUOTES = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "First, solve the problem. Then, write the code.",
    "Experience is the name everyone gives to their mistakes.",
    "In theory, theory and practice are the same. In practice, they’re not."
]

def get_random_quote():
    return random.choice(QUOTES)

if __name__ == "__main__":
    print(" Quote of the Day:")
    print(get_random_quote())

