number = 9
tries = 0

guess = int(input('what number is it?'))

for tries in range (0,3):
    if guess < number:
        guess = int(input('guess higher:'))
    elif guess > number:
        guess = int(input('guess lower:'))
    else:
        continue
print('the number is {}'.format(number))
