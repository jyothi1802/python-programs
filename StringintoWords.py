#Write a python program to given string split into list of words

def st():
    my_str = input("Enter a string: ")
     # breakdown the string into a list of words
    words = my_str.split()
    return words
    for word in words:
        print(word)
print(st())
