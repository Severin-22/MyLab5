import re
def custom_sort(words):

    def sorting_key(word): # пріоритет сортування визначається
        
        if re.match(r'[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ]', word): # Українські літери мають бути раніше за англійські
            return (0, word.lower())
        else:
            return (1, word.lower())

    return sorted(words, key=sorting_key)

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            first_sentence = re.split(r'(?<=[.!?])\s', content.strip())[0]
            print("Перше речення файлу:", first_sentence)

            words = re.findall(r'\b\w+\b', content) # змінна в якій зберігаю видалені знаки пунктуації та розділяю на слова

            sorted_words = custom_sort(words) # сортую

            space_count = content.count(' ') # зберігаю кількість слів, що вираховуються

            print("\nВідсортовані слова:", sorted_words)
            print("\nКількість слів:", len(sorted_words))
            print("\nКількість пробілів у файлі:", space_count)

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    file_path = input("Введіть шлях до текстового файлу: ")
    read_file(file_path)
