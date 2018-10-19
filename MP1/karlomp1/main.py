import engine
import interface

dictionary = engine.generate_dictionary()

def main(dictionary):

    while True:

        gamemode = interface.main_menu(dictionary[1])

        if gamemode == '1':
            print('\nLoading words...')
            interface.anagrams_main(gamemode, dictionary[0])

        if gamemode == '2':
            print('\nLoading words...')
            interface.wh_main(gamemode, dictionary[0])

        if gamemode == '3':
            dictionary = engine.generate_dictionary()

        elif gamemode == '4':
            break

if __name__ == '__main__':
    main(dictionary)
