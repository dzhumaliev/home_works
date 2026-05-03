

vowels = "aeiouаеёиоуыэюя"
consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщъь"


while True:
    word = input("Введите слово: ").lower()

    word_len = 0
   

    vowels_count = 0
    consonants_counts = 0

    if word == "выход":
        break
    else:
        for i in word:
            if i in vowels:
                vowels_count += 1
                word_len += 1
            
            elif i in consonants:
                consonants_counts += 1
                word_len += 1
            
        print(f'Количество букв: {word_len}')
        
        print(f'Согласных букв: {consonants_counts}')
        print(f'Гласных букв: {vowels_count}')

        print(f'Гласные/Согласные {round((vowels_count * 100) / word_len, 2)}% / {round((consonants_counts * 100) / word_len, 2)}%')

