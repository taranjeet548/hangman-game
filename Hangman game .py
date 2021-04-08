#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 
from collections import Counter
somewords="""apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon"""
somewords=somewords.split()
word=random.choice(somewords)
if __name__=="__main__":
    print("Guess the word! HINT: word is a name of a fruit")
    for i in word:
        print('_',end=" ")
    letterguessed=""
    correct=0
    flag=0
    chances=len(word)+2
    try:
        while (chances!=0) and (flag==0):
            chances-=1
            guess=str(input("Guess a letter "))
            if not guess.isalpha():
                print("enter a letter")
                continue
            elif len(guess)>1:
                print("enter a single letter")
                continue
            elif guess in letterguessed:
                print("letter already guessed")
                continue 
            if guess in word:
                k=word.count(guess)
                for _ in range(k):
                    letterguessed+=guess
            for char in word:
                if char in letterguessed and Counter(letterguessed)!=Counter (word):
                    print(char,end="")
                    correct+=1
                elif Counter(letterguessed)==Counter (word):
                    print("The word is:",word)
                    print ("Congratulations!,you won ")
                    flag=1
                    break
                    break
                else:
                    print("_",end="")
                    
            if (chances<=0) and Counter(letterguessed)!=Counter(word):
                print("You lost")
                print("The word was ",word)
    except KeyboardInterrupt:
        print("Better luck next time")
        exit()


# In[ ]:





# In[ ]:




