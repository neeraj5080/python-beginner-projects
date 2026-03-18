import random

# word list
words = ["python", "college", "project", "computer", "science"]

# random word choose
word = random.choice(words)

# word scramble karna
scrambled = "".join(random.sample(word, len(word)))

print("Word Scramble Game")
print("Unscramble the word")

print("Scrambled word:", scrambled)

guess = input("Your answer: ")

if guess == word:
    print("Correct! 🎉")
else:
    print("Wrong answer")
    print("Correct word was:", word)
