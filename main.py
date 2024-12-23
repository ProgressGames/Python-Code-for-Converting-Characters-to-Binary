word = input("Enter a word: ")

# Перебираем каждый символ в строке и выводим его букву и двоичный код
for char in word:
    binary_code = bin(ord(char))[2:]  # Получаем двоичный код символа
    print(f"Character: {char}, Binary code: {binary_code}")
