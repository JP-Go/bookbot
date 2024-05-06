def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_contents(book_path)
    word_count = count_words(contents)
    letter_frequency = calculate_letter_frequency(contents)
    report = generate_report(letter_frequency)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for report_item in report:
        print(f"The '{report_item["letter"]}' character was found {report_item["count"]} times")
    print(f"--- End report ---")


def get_book_contents(path):
    with open(path) as f:
        return f.read()

def count_words(content):
    return len(content.split())

def calculate_letter_frequency(content:str):
    letters = {}
    for letter in content:
        if not letter.isalpha():
            continue
        lowercased = letter.lower()
        letters[lowercased] = letters.get(lowercased,0) + 1
    return letters

def to_report_item(letter,count):
    return {
        "letter": letter,
        "count": count
    }
def sort_by(item):
    return item["count"]

def generate_report(letter_fequency):
    report = [to_report_item(letter, letter_fequency[letter]) for letter in letter_fequency ]
    report.sort(key=sort_by, reverse=True)
    return report

if __name__ == "__main__":
    main()
