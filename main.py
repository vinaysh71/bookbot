def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    l_text = text.lower()
    res = {}
    for c in l_text:
        if res[c]:
            res[c] += 1
        else:
            res[c] = 1

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(count_words(file_contents))

main()