#ДРЕВО ИСКЛЮЧЕНИЙ
#BaseException
# +-- SystemExit
# +-- KeyboardInterrupt
# +-- GeneratorExit
# +-- Exception
#  	 +-- StopIteration
#  	 +-- StopAsyncIteration
#  	 +-- ArithmeticError
#  	 |	FloatingPointError
#  	 |	OverflowError
#  	 |	ZeroDivisionError
#  	 +-- AssertionError
#  	 +-- AttributeError
#  	 +-- BufferError
#  	 +-- EOFError
#  	 +-- ImportError
#  	 |	+-- ModuleNotFoundError
#  	 +-- LookupError
#  	 |	+-- IndexError
#  	 |	+-- KeyError
#  	 +-- MemoryError
#  	 +-- NameError
#  	 |	+-- UnboundLocalError
#  	 +-- OSError
#  	 |	+-- BlockingIOError
#  	 |	+-- ChildProcessError
#  	 |	+-- ConnectionError
#  	 |	|	+-- BrokenPipeError
#  	 |	|	+-- ConnectionAbortedError
#  	 |	|	+-- ConnectionRefusedError
#  	 |	|	+-- ConnectionResetError
#  	 |	+-- FileExistsError
#  	 |	+-- FileNotFoundError
#  	 |	+-- InterruptedError
#  	 |	+-- IsADirectoryError
#  	 |	+-- NotADirectoryError
#  	 |	+-- PermissionError
#  	 |	+-- ProcessLookupError
#  	 |	+-- TimeoutError
#  	 +-- ReferenceError
#  	 +-- RuntimeError
#  	 |	    +-- NotImplementedError
#  	 |	    +-- RecursionError
#  	 +-- SyntaxError
#  	 |	    +-- IndentationError
#  	 |      +-- TabError
#  	 +-- SystemError
#  	 +-- TypeError
#  	 +-- ValueError
#  	 |	    +-- UnicodeError
#  	 |     	+-- UnicodeDecodeError
#  	 |     	+-- UnicodeEncodeError
#  	 |     	+-- UnicodeTranslateError
#  	 +-- Warning
#    +-- DeprecationWarning
#    +-- PendingDeprecationWarning
#    +-- RuntimeWarning
#    +-- SyntaxWarning
#    +-- UserWarning
#    +-- FutureWarning
#    +-- ImportWarning
#    +-- UnicodeWarning
#    +-- BytesWarning
#    +-- ResourceWarning)

#1
try:
    raise ZeroDivisionError # возбуждаем исключение ZeroDivisionError
except ArithmeticError: # ловим его родителя
    print("Hello from arithmetic error")

#2 не лучший вартиант
try:
    raise ZeroDivisionError
except ArithmeticError:
    print("Arithmetic error")
except ZeroDivisionError:
    print("Zero division error")

#3 вот так правильнее потому что лучше ловить сначала потомка а потом родителя
try:
    raise ZeroDivisionError
except ZeroDivisionError: # сначала пытаемся поймать потомка
    print("Zero division error")
except ArithmeticError: # потом уже ловим предка
    print("Arithmetic error")

#4Создадим своё исключение и поймаем его
class MyException(Exception):  # создаём пустой класс – исключения
    pass

try:
    raise MyException("message")  # поднимаем наше исключение
except MyException as e:  # ловим его за хвост как шкодливого котёнка
    print(e)  # выводим информацию об исключении


#5 Создадим исключение с наследованием и поймаем его
class ParentException(Exception):  # создаём пустой класс – исключения потомка, наследуемся от exception
    pass

class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    pass

try:
    raise ChildException("message")  # поднимаем исключение-наследник
except ParentException as e:  # ловим его родителя
    print(e)  # выводим информацию об исключении


#6 Можно добавить собственные аргументы в конструктор
class ParentException(Exception):
    def __init__(self, message,
                 error):  # допишем к нашему пустому классу конструктор, который будет печатать дополнительно в консоль информацию об ошибке.
        super().__init__(message)  # помним про вызов конструктора родительского класса
        print(f"Errors: {error}")  # печатаем ошибку

class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    def __init__(self, message, error):
        super().__init__(message, error)

try:
    raise ChildException("message", "error")  # поднимаем исключение-наследник, передаём дополнительный аргумент
except ParentException as e:
    print(e)  # выводим информацию об исключении



######
class NonPositiveDigitException(ValueError):
    pass

class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Неправильно указанна сторона квадрата')