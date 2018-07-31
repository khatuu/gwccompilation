def display(word, already_guessed_letters):
    new_str = ""
    for letter in phrase:
        if letter in already_guessed_letters:
            new_str += letter
        elif letter == " " :
            new_str += "  "
        else:
            new_str += "_ "
    return new_str

def main():
    print_beginning_of_game()

# have a word/phrase
phrase = "girls who code"

# keep track of user's guesses
guessed_letters = []
game_over = False

beginning = display(phrase, guessed_letters)
print(beginning)

while game_over != True:
    guess = input("Enter a letter: ")
    if guess in phrase:
        print("You got a letter: {}".format(guess))
    else :
        print("{} is not in the phrase".format(guess))

    guessed_letters.append(guess)

    wakeup = display(phrase, guessed_letters)
    print(wakeup)

    display = ""
    for letter in phrase:
        if letter in guessed_letters:
            display += letter
        elif letter == " " :
            display += "  "
        else:
            display += "_ "
    print(display)

    game_over = True
    for d in display:
        if d == "_" :
            game_over = False

print("END OF GAME")


# end game if user gets all right letters in word/phrase
