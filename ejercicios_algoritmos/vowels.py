def count_vowels(words):
    count = 0
    total_value = 0
    try:
        words = [each_string.lower() for each_string in words]
    except AttributeError:
        return 'Solo se pueden recibir palabras'

    for word in words:
        for letter in word:
            if letter in ('a', 'e', 'i', 'o', 'u'):
                count += 1
        if count != 0:
            if count % 2 == 0:
                total_value += 2
            else:
                total_value += 1
        count = 0
    return total_value


list_words = ['nm', 'e', 'tren', 'mundo', 'hola', 'a', 9]

print(count_vowels(list_words))
