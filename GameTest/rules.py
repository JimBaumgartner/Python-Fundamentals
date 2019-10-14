def hangman(count, display, word):
    limit = 5
    guess = input('the word is ' + display + ' Enter your guess' )
    if guess in word:
        index = word.find(guess)
        word = word(index) + '*' + word[index + 1:]
        display = display[index] + guess + display[index + 1:]
else:
    count == 1:
    print('Nope , not in there'  = str(limit - count))
    
    