def is_even(num):

    return num%2 == 0





def slugify(phrase):

    return phrase.lower().strip().replace(" ","-")



def vowels(word):

    count =0

    for char in word:

        if char in "aeiou":

            count +=1

    return count



def slugify(phrase="Hello I love you",sep="-"):

    return phrase.lower().strip().replace(" ",sep)