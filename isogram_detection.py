def is_isogram(string):
    if type(string) == str and string.isalpha():
        s = string.lower()
        if len(set(s)) == len(s): 
            print('Entered string is an isogram and the length equals %d' % len(s))
        else:
            print('Entered string is not an isogram')
    else:
        return print('Entered text is either empty, not a string or contains numbers')

string = input("Enter string to check if it's an isogram: ")
is_isogram(string)
