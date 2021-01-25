import random
from Words import all_words

def play():

    l=0
    word=valid_words(all_words)
    if len(word)<7:
        no_of_lives=7
    else:
        no_of_lives=10

    used_words=set()
    temp=list(' -'*len(word)+' ')

    print("\nWelcome to the hangman game !! ")
    print(f"You have {no_of_lives} lives to guess a {len(word)} letter word !! \n")

    while no_of_lives:

        print("Word :",*temp,'\n')

        if len(used_words):
            print("You have already chosen these letters :",*used_words)
            print(f"{no_of_lives} lives remaining !! \n")
        
        cur_letter=input("Input a letter which u think might be in the word : ")
        used_words.add(cur_letter)
        pos=get_positions(cur_letter,word)
        
        if not pos:
            no_of_lives-=1

        for i in range(len(pos)):
            temp[pos[i]]=cur_letter
            l+=1
        
        if l==len(word):

            print("\nCongratulations , You won the game !! ")
            print(f"The word was indeed {word}\n")
            break
    
    else:
        print("\nSorry,You lost the game !! ")
        print(f"The word was {word}\n")

def valid_words(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word

def get_positions(l,word):
    indices=[]
    for i in range(len(word)):
        if word[i]==l:
            indices.append(2*i+1)

    return indices

play()