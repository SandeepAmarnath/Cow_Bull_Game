import enchant #Library to generate or search in english dictionary
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def check_word(): #Generates a random word
    while True:
        pick = random.sample(letters, 5)
        word=''.join(pick)
        d = enchant.Dict("en_US")
        check_word=d.check(word)
        if check_word==True:
            return word
word=check_word()
chance=1

def input_word(word,chance): #User inputs the new word and checks cows and bulls
    guess=input("Enter a 5 letter word:: ")

    cow=0
    bull=0


    for i in range(len(word)):
        if guess[i] in word:
            if guess[i]==word[i]:
                bull +=1
            else:
                cow+=1
    print("Cows are {}".format(cow))
    print("Bulls are {}".format(bull))
    print("The word is "+word)
    if chance==1:
        print("You have compeleted {} chance".format(chance))
    else:
        print("You have compeleted {} chances".format(chance))
    if chance==10 and bull!=5:
        print("Sorry, You lost the game")
        exit()
    if chance<=10 and bull==5:
        print("You won the game")
        exit()
    if chance<=10 and bull!=5:
        chance+=1
        input_word(word,chance)


input_word(word,chance)



