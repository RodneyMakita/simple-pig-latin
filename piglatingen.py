def pig_it(text):
    words = text.split()
    pig_latin_words = []
    for word in words:
        if word.isalpha():  # Check if the word contains only letters
            pig_latin_word = word[1:] + word[0] + 'ay'
        else:
            pig_latin_word = word
        pig_latin_words.append(pig_latin_word)
    return ' '.join(pig_latin_words)

