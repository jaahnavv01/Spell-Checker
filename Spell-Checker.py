from textblob import TextBlob  #importing the library 

t = 1
while t:
    a = input("enter the word to be checked: ") #incorrect spelling
    print("original text: ",str(a))                

    b = TextBlob(a) #correcting the text

    print("corrected spelling: ", str(b.correct())) #prints corrected text
    t = int(input("TRY AGAIN? 1 : 0 "))