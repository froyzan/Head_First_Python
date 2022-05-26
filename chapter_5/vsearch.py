#!/usr/bin/python3
def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'.
       Возвращает набор 'букв', найденных во 'фразе'."""
    return set(letters).intersection(set(phrase))
