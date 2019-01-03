#Write a python program to given string split into list of sentences and words 

def st():
    my_str = input("Enter a string: ")
    # breakdown the string into a list of words
    words = my_str.split()
     # breakdown the string into a list of sentences
    sentence = my_str.split(".")
    print(sentence)
    print(len(sentence))
    return words
    for word in words:
        print(word)
print(st())
