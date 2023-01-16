import random
from words import words
from visuals import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # random kiválaszt egy szót
    while '-' in word or ' ' in word: #akasztófában nem tudunk kötőjelet vagy szóközt kitalálni ezért addig keres egy szót amíg az nem valid
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # milyen betűk vannak a szóban
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # azok a betűk amiket a felhasználó adott meg

    lives = 7

    # felhasználói input-ot kérünk
    while len(word_letters) > 0 and lives > 0: #addig tippeljen a használó amíg ki nem találta a szót vagy elfogy az összes élete
        # kiírja, hogy hány élete maradt
        # és milyen betűket használt már a játékos (vesszővel és szóközzel elválasztva)
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # kiírja a szót az eltalált betűkkel és egy kötőjelet rak a még ki nem talált bető helyére
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list)) #láncot csinál

        user_letter = input('Guess a letter: ').upper() #bekér egy betűt
        if user_letter in alphabet - used_letters: #ha tippel egy betűt, akkor a használtak közé rakja
            used_letters.add(user_letter)
            if user_letter in word_letters: #ha a tippelt betű benne van a szóban, kiszedi a szóban lévő betűkből, hogy azt már ne lehessen kitalálni
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # elvesz egy életet rossz tipp esetén
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters: #ha ugyanazt tippelik
            print('\nYou have already used that letter. Guess another letter.')

        else: #ha esetleg olyat tippelnek ami nincs benne az angol abc-ben
            print('\nThat is not a valid letter.')

    if lives == 0: #ha elfogy az élet akkor ezeket írja ki
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!') #ha sikerül kitalálni a szót, ezt írja ki
        
if __name__ == '__main__':
    hangman()
