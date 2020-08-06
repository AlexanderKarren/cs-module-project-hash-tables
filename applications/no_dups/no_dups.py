def no_dups(s):
    my_cache = {}
    words = s.split()
    new_string = ""
    for i in range(len(words)):
        if words[i] not in my_cache:
            my_cache.update({words[i]: True})
            new_string += (words[i] + " ")
    return new_string[0:-1]


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
