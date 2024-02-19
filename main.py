def main():
    book_path = input("Welches der folgenden Bücher wollen sie analysieren? books/Romeo&Juliet.txt, books/Frankenstein.txt oder books/GoT.txt: ")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Beginne die Buchstabenzählung von {book_path} ---")
    print(f"{num_words} Wörter wurden gefunden")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"Der Buchstabe '{item['char']}' wurde {item['num']} mal gefunden")

    print("--- Beende Buchstabenzählung ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()