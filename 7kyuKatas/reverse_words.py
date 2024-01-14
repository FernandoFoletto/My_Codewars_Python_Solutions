
text = "The quick brown fox jumps over the lazy dog."


def reverse_words(text):
    words = text.split(' ')
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' '.join(reversed_words)
    return reversed_string

    
