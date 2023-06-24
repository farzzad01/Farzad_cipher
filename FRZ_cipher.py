def reverse_word(word):
    return word[::-1]

def reflector(word):
    reflected_word = ""
    for letter in word:
        reflected_letter = chr(ord('z') - (ord(letter.lower()) - ord('a')))
        reflected_word += reflected_letter.upper() if letter.isupper() else reflected_letter
    return reflected_word

def letters_to_numbers(word):
    numbers = []
    for letter in word:
        if letter.isalpha():
            number = ord(letter.lower()) - ord('a') + 1
            numbers.append(number)
    return numbers


