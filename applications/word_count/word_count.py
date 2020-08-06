def word_count(s):
    count_hash = {}
    ignore = '":;,.-+=/\\|[]{}()*^&'
    words = s.split()
    for i in range(len(words)):
        clean_word = ''.join(j for j in words[i].lower() if not j in ignore)
        if len(clean_word) > 0:
            if clean_word not in count_hash:
                count_hash.update({clean_word: 1})
            else:
                count_hash.update({clean_word: count_hash[clean_word] + 1})
    return count_hash


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
