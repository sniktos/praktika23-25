from abc import ABC, abstractmethod

# Абстрактный продукт
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Конкретный продукт
class ConcreteProductA(Product):
    def operation(self):
        return "Product A"

class ConcreteProductB(Product):
    def operation(self):
        return "Product B"

# Абстрактный создатель
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: Работает с {product.operation()}"

# Конкретный создатель
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()
