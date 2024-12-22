from abc import ABC, abstractmethod

# Абстрактный класс для анализа текста
class TextAnalyzer(ABC):
    @abstractmethod
    def analyze(self, text: str) -> tuple:
        pass

# Конкретный класс для подсчета гласных и согласных
class VowelConsonantAnalyzer(TextAnalyzer):
    def init(self):
        self.vowels = set("aeiouAEIOU")

    def analyze(self, text: str) -> tuple:
        words = text.split()
        result = []
        total_vowels = 0

        for word in words:
            vowel_count = sum(1 for char in word if char in self.vowels)
            consonant_count = sum(1 for char in word if char.isalpha() and char not in self.vowels)
            total_vowels += vowel_count
            result.append((word, vowel_count, consonant_count))

        return result, total_vowels

# Фабрика для создания анализаторов текста
class TextAnalyzerFactory:
    @staticmethod
    def create_analyzer(analyzer_type: str) -> TextAnalyzer:
        if analyzer_type == 'vowel_consonant':
            return VowelConsonantAnalyzer()
        else:
            raise ValueError("Unknown analyzer type")

# Класс для функции analyze_text
class AnalyzeText:
    @staticmethod
    def analyze_text(text: str) -> tuple:
        factory = TextAnalyzerFactory()
        analyzer = factory.create_analyzer('vowel_consonant')
        result, total_vowels = analyzer.analyze(text)
        return result, total_vowels

# Пример использования
if name == "main":
    text = "This is an example text with some repeated words."
    result, total_vowels = AnalyzeText.analyze_text(text)
    print("Результат анализа:")
    for word, vowel_count, consonant_count in result:
        print(f"Слово: {word}, Гласные: {vowel_count}, Согласные: {consonant_count}")
    print(f"Общее количество гласных в тексте: {total_vowels}")