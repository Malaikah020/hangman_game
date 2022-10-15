# ScriptName: my_functions.py
# Author: Malaikah Hafeez 121344326

# make a function in which you can play hangman using a file that contains all the words.
# the words should be in a list and then a random one should be chosen and then you use it as secret word.
# let user input letters - letterguessed and see if they are in the secret word if they are 
# add them to ans if not remove letter from alphabet and print
# if there is no letters left to guess return congrats
# if you've used all you guesses return you killed hangman
# -------------------------------------------------------------------------------------------------------
import random
# rename file
WORDLIST_FILENAME = "words.txt"

# def word_file():
#     """
#     from a word file to a list to give the list of words that the hangman could be thinking
#     """
#     # inFile: file
#     inFile = open(WORDLIST_FILENAME, 'r')
#     # line: string
#     line = inFile.readline()
#     # wordlist: list of strings
#     wordlist = line.split()
#     # print("  ", len(wordlist))
#     return wordlist

# function i used if my file was not there
# def word_file():
#     """
#     from a word file to a list to give the list of words that the hangman could be thinking
#     """
#     wordlist = ["fizz", "buzz", "jink", "hajj", "quiz","able","acid","aged","also","area","army","away","baby","back","ball","band","bank","base","bath","bear","beat","been","beer","bell","belt","best","bill","bird","blow","blue","boat","body","bomb","bond","bone","book","boom","born","boss","both","bowl","bulk","burn","bush","busy","call","calm","came","camp","card","care","case","cash","cast","cell","chat","chip","city"]
    
#     return wordlist




# -----------------------------------

# get a word list from the wordfile function to use 
# wordlist = word_file()
# generate a random word from the word list just created
# secretWord=random.choice(wordlist)
# secretWord1 = secretWord.lower()

def getGuessedWord(secretWord:str, lettersGuessed:str)->str: 
    '''
    check if the letter guessed is in the secret word and if so add to the answer and replace "_"
    '''
    # make a list
    s=[]
    # if in word append i
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    # string to add to
    ans=''
    # if letter in word add to ans otherwise add a _
    for i in secretWord:
        if i in s:
            ans+=i
        else:
            ans+='_ '
    return ans



def getAvailable_L(lettersGuessed:str)->str:
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed. basically the alphabet not guessed.
    '''
    # import string
    import string
    # remove letter guessed from alphabet using a for loop
    ans=list(string.ascii_lowercase)
    for i in lettersGuessed:
        ans.remove(i)
    # join the list of alphabets into a string
    return ''.join(ans)

# to prevent from cheating i added the file function in the main funtion
# def hangman(secretWord)
def hangman(l:int=2):
    '''
    params are nothing or 2 
    main function to call to play the game which is what you see when you play.
    it counts the mistakes made and what messages should be returned if you right, wrong, have won or lost.
    
    '''
    # error handler
    try:
        if l == 2:
            # inFile: file
            inFile = open(WORDLIST_FILENAME, 'r')
            # line: string
            line = inFile.readline()
            # wordlist: list of strings
            wordlist = line.split()
            # print("  ", len(wordlist))
            secretWord=random.choice(wordlist)
            secretWord = secretWord.lower()
            
            # welcome message and tells you how long the word is
            print("\n Welcome to the game, Hangman!")
            print("I am thinking of a word that is",len(secretWord),"letters long.")
            global lettersGuessed
            # start with 0 mistakes
            mistakeMade=0
            # add the letter guessed in a list
            lettersGuessed=[]
            # runs until you are 0
            while 10 - mistakeMade > 0:
                # if you don't have any _ print congrats and word and message 
                if '_' not in getGuessedWord(secretWord, lettersGuessed):
                    print("-------------\n")
                    print("Congratulations, you won!")
                    print("The word was",secretWord+"!")
                    print("You saved hangman!")
                    print("    \(º.º)/    ")
                    print("     \ | /    ")
                    print("      / \    ")
                    print("     '   '   ")
                    break
                # if their is _ then print how many guesses you have left and then the rest of the alphabet left 
                else:
                    print("-------------\n")
                    print("You have",10-mistakeMade,"guesses left.")
                    print("Available letters:",getAvailable_L(lettersGuessed))
                    # get the input letter as guess
                    guess=str(input("Please guess a letter: ")).lower()
                    # if the letter already guessed 
                    if guess in lettersGuessed:
                        print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
                    # if the letter is in secret word but not in letter already guessed
                    elif guess in secretWord and guess not in lettersGuessed:
                        # add to letter guessed
                        lettersGuessed.append(guess)
                        print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
                    # if not in guessed list and not in secret word 
                    else:
                        lettersGuessed.append(guess)
                        mistakeMade += 1
                        print("Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed))
                # if you run out of guessed print lost message  
                if 10 - mistakeMade == 0:
                    print("-------------")
                    print("Sorry, you ran out of guesses. The word was",secretWord+'.')
                    print("YOU KILLED HANGMAN.")
                    print("      +---+    ")
                    print("      |   |    ")
                    print("    (-_-) |    ")
                    print("     /|\  |    ")
                    print("     / \  |    ")
                    print("    '   ' |    ")
                    print("   =========   ")
                    break
            
                else:
                    continue
        else:
            return "Oops something went wrong run again"
    except:
        return "Oops something went wrong run again"



# to play the game use the function hangman







    # ---------------------------------------------------------------------------------------






     

