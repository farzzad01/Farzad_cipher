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

def add_numbers(numbers, key_numbers):
    added_numbers = []
    key_length = len(key_numbers)
    for i in range(len(numbers)):
        new_number = (numbers[i] + key_numbers[i % key_length] - 1) % 26 + 1
        added_numbers.append(new_number)
    return added_numbers

def numbers_to_letters(numbers):
    word = ""
    for number in numbers:
        letter = chr(number + ord('a') - 1)
        word += letter
    return word

def encrypt(word, key_numbers):
    reversed_word = reverse_word(word)
    reflected_word = reflector(reversed_word)
    numbers = letters_to_numbers(reflected_word)
    added_numbers = add_numbers(numbers, key_numbers)
    encrypted_word = numbers_to_letters(added_numbers)
    reflected_encrypted_word = reflector(encrypted_word)
    return reflected_encrypted_word

def run():
      # key exapmle (N G R) -> (14 , 7 , 18)
    word = input("Enter a word or text to encrypt: ")
    key = input("Enter the key numbers (): ")
    key_numbers = [int(k) for k in key.split()]
    encrypted_word = encrypt(word, key_numbers)
    print("Encrypted word: ", encrypted_word)

run()
