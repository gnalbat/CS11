from os import system, name
from random import shuffle
import engine

'''''''''
Init
'''''''''

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

'''''''''''''''
Main Menu
'''''''''''''''

def main_menu(dictionary_name):
    clear()
    print('-' * 50)
    print('Totally not TextTwist nor Wordscapes')
    print('Current dictionary: ' + dictionary_name)
    print('-' * 50)
    print('Select Option:')
    print('1 Anagram Hunt')
    print('2 Word Hunt')
    print('3 Change Dictionary')
    print('4 Exit Game')
    print('-' * 50)
    gamemode = input('')
    return gamemode

'''''''''''''''
Anagrams
'''''''''''''''

def anagrams_main(gamemode, dictionary):
    word = engine.pick_words(gamemode, dictionary)
    anagrams = engine.find_anagrams(word, dictionary)
    hps = engine.hps(anagrams)
    score = 0
    while score == hps:
        word = engine.pick_words(gamemode, dictionary)
        anagrams = engine.find_anagrams(word, dictionary)
        hps = engine.hps(anagrams)
    anagrams_fn(score, word, hps, anagrams)

def anagrams_fn(score, word, hps, anagrams):
    inplay = True
    lives = 3
    done = []
    incorrect = []
    remaining = anagrams
    while (score != hps) and (lives > 0):
        clear()
        anagrams_print(inplay, score, hps, lives, word, done, incorrect, remaining)
        userinput = input()
        userinput = userinput.lower()
        if userinput in anagrams:
            score += engine.points(userinput)
            done.append(userinput)
            del remaining[remaining.index(userinput)]
        elif userinput in done:
            score += 0
        elif userinput == '' or ' ' in userinput:
            score += 0
        else:
            incorrect.append(userinput)
            lives -= 1

    clear()
    inplay = False
    anagrams_print(inplay, score, hps, lives, word, done, incorrect, remaining)
    input('Press enter key to return to main menu.')

def anagrams_print(inplay, score, hps, lives, word, done, incorrect, remaining):
    if inplay == False:
        if lives == 0:
            print('GAME OVER')
        else:
            print('GAME FINISED')
        print('-' * 50)
        print('GAME SUMMARY')

    print('-' * 50)

    if lives == 0:
        print('Score: ' + str(score) + ' / ' + str(hps) + '\n')
    else:
        print('Score: ' + str(score) + ' / ' + str(hps) + '\t' + 'Tries remaining: ' + str(lives) + '\n')

    print('Word to unscramble: ' + word + '\n')
    print('Correct guesses: ' + ' '.join(done) + '\n')
    print('Incorrect guesses: ' + ' '.join(incorrect))

    if inplay == False and lives == 0:
        print('\n' + 'Words unguessed: ' + ' '.join(remaining))

    print('-' * 50)

    if inplay == False and lives != 0:
        print('\n' + 'Congratulations, you won the game!')
    elif inplay == False and lives == 0:
        print('\n' + 'Better luck next time!')

'''''''''''''''
Word Hunt
'''''''''''''''
def wh_main(gamemode, dictionary):
    words = engine.pick_words(gamemode, dictionary)
    merged = engine.merge(words)
    jumbled = list(merged)
    shuffle(jumbled)
    jumbled = ' '.join(jumbled)
    answers = engine.wh_answers(dictionary, merged)
    hps = engine.hps(answers)
    score = 0
    wh_fn(score, merged, hps, answers, dictionary, jumbled)

def wh_fn(score, word, hps, answers, dictionary, jumbled):
    inplay = True
    lives = 3
    done = []
    incorrect = []
    remaining = answers
    while (score != hps) and (lives > 0):
        clear()
        wh_print(inplay, score, hps, lives, word, done, incorrect, remaining, jumbled)
        userinput = input()
        userinput = userinput.lower()
        if userinput in answers:
            score += engine.points(userinput)
            done.append(userinput)
            del remaining[remaining.index(userinput)]
        elif userinput in done:
            score += 0
        elif userinput == '' or ' ' in userinput:
            score += 0
        else:
            incorrect.append(userinput)
            lives -= 1

    clear()
    inplay = False
    wh_print(inplay, score, hps, lives, word, done, incorrect, remaining, jumbled)
    input('Press enter key to return to main menu.')

def wh_print(inplay, score, hps, lives, word, done, incorrect, remaining, jumbled):
    if inplay == False:
        print('GAME FINISHED')
        print('-' * 70)
        print('GAME SUMMARY')

    print('-' * 70)

    if inplay == True:
        print('Score: ' + str(score) + ' / ' + str(hps) + '\t' + 'Tries remaining: ' + str(lives) + '\n')
    else:
        print('Score: ' + str(score) + ' / ' + str(hps) + '\n')

    print('Letters to unscramble: ' + jumbled + '\n')
    print('Correct guesses: ' + ' '.join(done) + '\n')
    print('Incorrect guesses: ' + ' '.join(incorrect))

    if inplay == False and lives == 0:
        print('\n' + 'Words unguessed: ' + ' '.join(remaining))

    print('-' * 70)

    if inplay == False and lives != 0:
        print('\n' + 'Congratulations, you won the game!')
    elif inplay == False and lives == 0:
        print('\n' + 'Better luck next time!')
