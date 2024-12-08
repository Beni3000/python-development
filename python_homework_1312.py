import string
from collections import Counter


def read_poem_file():
    """Читает файл poem.txt и возвращает его содержимое."""
    with open('poem.txt', 'r', encoding='utf-8') as file:
        return file.readlines()


def count_total_characters(lines):
    """Считает общее количество символов в тексте."""
    return sum(len(line) for line in lines)


def count_letters(lines):
    """Считает количество букв (без пробелов и знаков препинания)."""
    text = ''.join(lines)
    return sum(c.isalpha() for c in text)


def count_total_lines(lines):
    """Считает общее количество строк в тексте."""
    return len(lines)


def count_non_empty_lines(lines):
    """Считает количество непустых строк в тексте."""
    return sum(1 for line in lines if line.strip())


def count_total_words(lines):
    """Считает общее количество слов в тексте."""
    return sum(len(line.split()) for line in lines)


def count_words_per_line(lines):
    """Возвращает количество слов в каждой строке."""
    return [len(line.split()) for line in lines]


def count_characters_per_line(lines):
    """Возвращает количество символов в каждой строке."""
    return [len(line) for line in lines]


def find_repeated_words(lines):
    """Находит повторяющиеся слова в тексте с указанием количества."""
    text = ''.join(lines).lower()
    words = text.split()
    word_counts = Counter(words)
    return {word: count for word, count in word_counts.items() if count > 1}


def letter_frequency(lines):
    """Проводит частотный анализ букв."""
    text = ''.join(lines).lower()
    letter_counts = Counter(c for c in text if c.isalpha())
    return dict(letter_counts)


def find_extra_symbols(lines):
    """Находит посторонние символы (пробелы и знаки препинания) и их количество."""
    text = ''.join(lines)
    symbols = Counter(c for c in text if not c.isalpha() and not c.isspace())
    spaces_count = text.count(' ')
    symbols['пробелов'] = spaces_count
    return dict(symbols)


def write_results_to_file(results):
    """Записывает результаты анализа в файл result.txt."""
    with open('result.txt', 'w', encoding='utf-8') as file:
        for line in results:
            file.write(line + '\n')


def main():
    # Читаем файл poem.txt
    lines = read_poem_file()

    results = []

    # 1. Сколько всего символов в тексте
    results.append(f"1. Всего символов в тексте - {count_total_characters(lines)}")

    # 2. Сколько букв в тексте (без пробелов и знаков препинания)
    results.append(f"2. Букв в тексте - {count_letters(lines)}")

    # 3. Сколько всего строк в тексте
    results.append(f"3. Всего строк в тексте - {count_total_lines(lines)}")

    # 4. Сколько непустых строк в тексте
    results.append(f"4. Непустых строк в тексте - {count_non_empty_lines(lines)}")

    # 5. Сколько всего слов в тексте
    results.append(f"5. Всего слов в тексте - {count_total_words(lines)}")

    # 6. Сколько слов в каждой строке
    word_counts = count_words_per_line(lines)
    results.append("6. Анализ слов по строкам:")
    for i, count in enumerate(word_counts, start=1):
        results.append(f"{i} строка - {count} слов")

    # 7. Сколько символов в каждой строке
    char_counts = count_characters_per_line(lines)
    results.append("7. Анализ символов по строкам:")
    for i, count in enumerate(char_counts, start=1):
        results.append(f"{i} строка - {count} символов")

    # 8. Найти повторяющиеся слова
    repeated_words = find_repeated_words(lines)
    results.append("8. Повторяющиеся слова:")
    for word, count in repeated_words.items():
        results.append(f"{word} - {count}")

    # 9. Частотный анализ букв
    letter_freq = letter_frequency(lines)
    results.append("9. Частотный анализ текста:")
    for letter, count in sorted(letter_freq.items()):
        results.append(f"{letter} - {count}")

    # 10. Найти все посторонние символы
    extra_symbols = find_extra_symbols(lines)
    results.append("10. Прочие символы:")
    for symbol, count in extra_symbols.items():
        results.append(f"{symbol} - {count}")

    # Записываем результаты в файл
    write_results_to_file(results)

    print("Анализ завершен. Результаты записаны в файл result.txt.")


# Запуск основной функции
main()
