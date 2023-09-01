import random
from constants import *
from english_words import get_english_words_set

lives = LIVES
words = [word for word in get_english_words_set(['web2'], lower=True) if len(word) > DIFFICULTY]
chosen_word = random.choice(words)
ans = ['_'] * len(chosen_word)
endgame = ENDGAME
result = WIN

print(logo)
print("Word Length:", len(chosen_word))
print(ans)
while not endgame:
    guess = input("Guess a letter: ").lower()

    for i, letter in enumerate(chosen_word):
        if guess == letter:
            ans[i] = letter
            if "_" not in ans:
                print(ans)
                endgame = True

    if guess not in chosen_word:
        lives -= 1
        if not lives:
            result = LOSE
            endgame = True

    print(ans)
    print(stages[lives])

print(result)
print(f"Solution: {chosen_word}")
print(ans)
