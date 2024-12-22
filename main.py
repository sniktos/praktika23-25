class WordCountAnalyzer:
    def analyze(self, text):
        return len(text.split())

class CharCountAnalyzer:
    def analyze(self, text):
        return len(text)

class UniqueWordAnalyzer:
    def analyze(self, text):
        return len(set(text.split()))

def main():
    text = "This is an example text with some repeated words."
    analyzers = [WordCountAnalyzer(), CharCountAnalyzer(), UniqueWordAnalyzer()]

    for analyzer in analyzers:
        print(f"{analyzer.__class__.__name__}: {analyzer.analyze(text)}")

if __name__ == "__main__":
    main()
