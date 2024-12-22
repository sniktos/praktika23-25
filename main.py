def word_count(text):
    return len(text.split())

def char_count(text):
    return len(text)

def unique_word_count(text):
    return len(set(text.split()))

def main():
    text = "This is an example text with some repeated words."
    print(f"Word count: {word_count(text)}")
    print(f"Character count: {char_count(text)}")
    print(f"Unique word count: {unique_word_count(text)}")

if __name__ == "__main__":
    main()
