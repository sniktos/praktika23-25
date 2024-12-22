from abc import ABC, abstractmethod

# Абстрактный анализатор
class TextAnalyzer(ABC):
    @abstractmethod
    def analyze(self, text: str):
        pass

# Конкретные анализаторы
class WordCountAnalyzer(TextAnalyzer):
    def analyze(self, text: str):
        return len(text.split())

class CharCountAnalyzer(TextAnalyzer):
    def analyze(self, text: str):
        return len(text)

class UniqueWordAnalyzer(TextAnalyzer):
    def analyze(self, text: str):
        return len(set(text.split()))

# Абстрактный создатель
class AnalyzerFactory(ABC):
    @abstractmethod
    def create_analyzer(self) -> TextAnalyzer:
        pass

# Конкретные создатели
class WordCountFactory(AnalyzerFactory):
    def create_analyzer(self) -> TextAnalyzer:
        return WordCountAnalyzer()

class CharCountFactory(AnalyzerFactory):
    def create_analyzer(self) -> TextAnalyzer:
        return CharCountAnalyzer()

class UniqueWordFactory(AnalyzerFactory):
    def create_analyzer(self) -> TextAnalyzer:
        return UniqueWordAnalyzer()

# Использование
def main():
    text = "This is an example text with some repeated words."

    factories = [WordCountFactory(), CharCountFactory(), UniqueWordFactory()]
    for factory in factories:
        analyzer = factory.create_analyzer()
        print(f"{analyzer.__class__.__name__}: {analyzer.analyze(text)}")

if __name__ == "__main__":
    main()
