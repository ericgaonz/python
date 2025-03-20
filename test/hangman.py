import random

word_categories = {
    'Science': [
        'Velocity',
        'Momentum',
        'Force',
        'Gravity',
        'Mass',
        'Trajectory',
        'Projectile'
    ],
    'Maths': [
        'Sum',
        'Addition',
        'Multiplication',
        'Division',
        'Algebra',
        'Exponents',
        'Integers'
    ],
    'Tech': [
        'Control',
        'Loop',
        'Iteration',
        'Data Types',
        'Input',
        'Output',
        'Operators'
    ],
}

def main():
    userName = get_name()

    willing_check()
    
    familiar_with_game_check()

    chosen_category = get_chosen_category()
    
    selected_word = random.choice(word_categories[chosen_category])
    length_word = len(selected_word)
    word_underscores = ['_'] * length_word

    AmountOfTempts = 7
    incorrect_guesses = 0
    guessed_letters = []

    print(f'You have chosen: {chosen_category}. The random word chosen has {len(selected_word)} letters.')

    state = word_underscores
    print()
    print(' '.join(state))

    while incorrect_guesses < AmountOfTempts and '_' in word_underscores:
        guess = input('\nGuess a letter: ')

        if guess in guessed_letters:
            print('You have already guessed this letter. Try another one.')
            continue
        
        guessed_letters.append(guess)

        if guess in selected_word:
            new_state = list(word_underscores)
            indices = [i for i, letter in enumerate(selected_word) if letter == guess]
            for i in indices:
                new_state[i] = guess

            word_underscores = new_state
            print()
            print(' '.join(new_state))
        else:
            incorrect_guesses += 1
            print(f'\nIncorrect guesses remaining: {AmountOfTempts - incorrect_guesses}')
            draw_tree(incorrect_guesses)

            state = word_underscores
            print()
            print(' '.join(state))


    if (incorrect_guesses == 7):
        print('\nSorry %s, You Failed! The word is "%s"' % (userName, selected_word))
    else:
        print('\nWell Done, %s!!!! YOU DID IT!' % userName)


def get_name():
    while True:
        userName = input("\nPlease enter your name: ")
        if all(x.isalpha() or x.isspace() for x in userName):
            print("Hello %s!" % userName)
            break
        else:
            print('That is a invalid name, please retry again using letters only')
    
    return userName


def willing_check():
    while True:
        willing_to_play = input('\nAre you willing to play Hangman? (y/n): ')
        if willing_to_play == 'n':
            print('Maybe next time!')
            exit()
        elif willing_to_play == 'y':
            print('Great!')
            break
        else:
            print('That is an invalid input, please reinput.')


def familiar_with_game_check():
    while True:
        familiar_with = input('\nAre you familiar with playing Hangman? (y/n): ')
        if familiar_with == 'n':
            print('Hangman is a guessing game. You will be set a random word from one of the three categories, digital technology, maths or science of your choice. You will be able to guess any letter of your choice to try figure out the hidden word. You have 7 incorrect guesses till you lose. Good luck!')
            break
        elif familiar_with == 'y':
            print('Please select a category, which will be shown underneath!')
            break
        else:
            print('That is an invalid input, please reinput. ')


def get_chosen_category():
    while True:
        chosen_category = input('\nPlease input the category you would like to play, (Science, Maths, Tech): ')
        if chosen_category in word_categories:
            break
        else:
            print('That is not a category in the list, please input a proper one. ')

    return chosen_category


def draw_tree(times):
    if times <= 3:
        draw_repeat_part(times)

    if times == 4:
        print('  || = =')
        print('  |  /')
        print('  |/')
        print('  ||')
        draw_repeat_part(3)

    if times == 5:
        print('  || = = = = = = = = = = = = = =')
        print('  |  /')
        print('  |/')
        print('  ||')
        draw_repeat_part(3)
    
    if times == 6:
        print('  || = = = = = = = = = = = = = =')
        print('  |  /                 |')
        print('  |/                   |')
        print('  ||                 {$ $}')
        draw_repeat_part(3)

    if times == 7:
        print('  || = = = = = = = = = = = = = =')
        print('  |  /                 |')
        print('  |/                   |')
        print('  ||                 {$ $}')
        print('  ||               /{  :  }\\')
        print('  ||                  |||')
        print('  ||                 <===>')
        draw_repeat_part(2)

    print()

def draw_repeat_part(times):
    for i in range(times):
        print('  ||')
        print('  ||')
        print('  ||')

main()
