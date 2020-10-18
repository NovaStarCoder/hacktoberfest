if __name__ == '__main__':
    s = input()
    length = len(s)
    
    #print True if has any alphanumeric characters. Otherwise, print False.
    flag = False
    for i in range(length):
        if s[i].isalnum():
            flag = True
            break
    print(flag)
    
    #print True if has any alphabetical characters. Otherwise, print False.
    flag = False
    for i in range(length):
        if s[i].isalpha():
            flag = True
            break
    print(flag)
    
    #print True if has any digits. Otherwise, print False.
    flag = False
    for i in range(length):
        if s[i].isdigit():
            flag = True
            break
    print(flag)

    #print True if has any lowercase characters. Otherwise, print False.
    flag = False
    for i in range(length):
        if s[i].islower():
            flag = True
            break
    print(flag)
    
    #print True if has any uppercase characters. Otherwise, print False.
    flag = False
    for i in range(length):
        if s[i].isupper():
            flag = True
            break
    print(flag)
