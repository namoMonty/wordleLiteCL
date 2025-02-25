import random
import colorama
import math

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

from wordfreq import zipf_frequency


NUMCHANCES = 6
WORDLENGTH = 5
INVALIDS = "0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
games = []
gameDict = {
    "Guesses": 0,
    "Outcome": "",
    "TheWord": "",
}

streak = 0
def main():

    print(Fore.CYAN + "*****************WELCOME TO WORDLE*****************")
    playgameInput = input("Would You Like to play.....(" + Fore.GREEN + "Y" + Fore.WHITE + "/" + Fore.RED + "N" + Fore.WHITE + ")")
    if (playgameInput.lower() == "n"):
        
        gameRunning = False
        print("Ok, great, have a nice day I guess")
    else:

        gameRunning = True
        # insturctions
        

    gamesplayed = 0
    while (gameRunning):
        words = openWordsFile()
        weightedWords = getWordsFreq()
        THEWORD = weightedWordChoice(weightedWords)
        print(THEWORD) #(if you want to be a cheater, cheater pumpkin eater)
        print(f"Welcome to Wordle! Guess the {WORDLENGTH}-letter word.")
        print("Hints: Green = correct letter and position, Yellow = correct letter but wrong position, Red = incorrect letter.")
        attempts = 1
        guess = input(f"Enter your {WORDLENGTH}-letter guess: ").lower()
        outcome = ""

        gamesplayed += 1
        # round-loop
        while(attempts < NUMCHANCES):
            if (guess == THEWORD):
                print("YOU GOT IT!! " + Fore.GREEN + guess.upper() + Style.RESET_ALL + " IS THE WORD")
                outcome = "WIN"
                break
            if isValid(guess,words):
                attempts += 1
                print("Guess " + str(attempts) + ":  " + compareWord(guess,THEWORD))
                guess = input("ENTER WORD:  ")
            else:
                guess = input("INVALID INPUT! ENTER NEW WORD:  ")

            if attempts >= NUMCHANCES:
                print("GAME OVER! THE WORD WAS....  " + Fore.BLUE + THEWORD.upper())
                outcome = "LOSS"
        
        game = {"game": "Game " + str(gamesplayed),"outcome":outcome,"theWord":THEWORD,"guesses":attempts}
        games.append(game)
        playgameInput = input("Would You Like to play Again? .....(" + Fore.GREEN + "Y" + Fore.WHITE + "/" + Fore.RED + "N" + Fore.WHITE + ")")
        for game in games:
            print(game)

        if (playgameInput.lower() == "n"):
            print("Ok, great, have a nice day I guess")
            gameRunning = False
            break
        else:
            gameRunning = True
        
# returns the frequency of words as a sorted list
def getWordsFreq():
    words = openWordsFile()

    wordsRanked = []
    for word in words:
        ranking = []
        wordRank = zipf_frequency(word, 'en')
        wordsRanked.append([word,wordRank])
    wordsRankedSorted = sorted(wordsRanked, key=lambda x:x[1], reverse=False)

    return wordsRankedSorted
# get words from wordlist as list
def openWordsFile():
    file = open("valid-wordle-words.txt",'r')
    content = file.read()
    file.close()
    wordList = content.split("\n")
    return wordList
# check if word is a word in word list and does not contain an invalid character
def isValid(word,wordList):
    word = word.lower()
    if word not in wordList:
        return False
    else:
        for char in word:
            if char in INVALIDS:
                return False
    return True

# pick a truly random word with no weight attached(if desired)
def pickRandomWord(wordList):
    random.shuffle(wordList)
    randomIndex = random.randint(0,len(wordList)-1)
    return wordList[randomIndex]
# weighted wordlist
def weightedWordChoice(wordList):
    # get words and ranks\
    words = [item[0] for item in wordList]
    ranks = [item[1] for item in wordList]

    totalRank = sum(ranks)
    weights = weights = [rank / totalRank for rank in ranks]

    chosenWord = random.choices(words,weights=weights,k=1)[0]
    return chosenWord
# user feedback on words
def compareWord(myWord,theWord):
    attempt = ""
    for letter in range(len(myWord)):
        if myWord[letter] == theWord[letter]:
            attempt = attempt + Fore.GREEN + myWord[letter].upper() + Style.RESET_ALL
        elif myWord[letter] in theWord:
            attempt = attempt + Fore.YELLOW + myWord[letter].upper() + Style.RESET_ALL
        else:
            attempt = attempt + Fore.RED + myWord[letter].upper() + Style.RESET_ALL
    return attempt

main()
























































