import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")

# Создаём функцию игры:
# рандомно выбранное определение слова переводится на русский язык
# пользователь предлагает свой вариант слова на английском языке, соответствующее определению.
# ответ пользователя оценивается на соответствие загаданному слову

def word_game():
    print("Добро пожаловать в игру")
    translator = Translator()  # Создаём объект переводчика

    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим определение на русский язык
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text

        # Начинаем игру
        print(f"Значение слова - {translated_definition}")
        user = input("Что это за слово? ")
        if user == word:  # Слово вводится на английском языке
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()

# УГАДАТЬ СЛОВО НЕРЕАЛЬНО ИЗ-ЗА НЕТОЧНОСТИ ПЕРЕВОДА ЕГО ОПРЕДЕЛЕНИЯ