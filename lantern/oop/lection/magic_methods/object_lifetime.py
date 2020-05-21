class Word(str):
    '''Класс для слов, определяющий сравнение по длине слов.'''

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] # Теперь Word это все символы до первого пробела
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)


if __name__ == "__main__":
    word = Word("abc")
    phrase = Word("Hello Student")

    print(word)
    print(phrase)

    print(word > phrase)
