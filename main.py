def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    l_text = text.lower()
    res = {}
    for c in l_text:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    
    print(res)
    

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(count_words(file_contents))

main()