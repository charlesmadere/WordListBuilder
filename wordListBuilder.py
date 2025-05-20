import os
from typing import Any, Collection, Final

MAIN_TEXT_FILE: Final[str] = 'banned_terms.txt'
NEW_WORDS_TEXT_FILE: Final[str] = 'new_words.txt'

if not os.path.exists(MAIN_TEXT_FILE) or not os.path.exists(NEW_WORDS_TEXT_FILE):
    raise FileNotFoundError(f'File not found: ({NEW_WORDS_TEXT_FILE=}) ({NEW_WORDS_TEXT_FILE=})')

mainTextFileWords: set[str] = set()
rawLines: Collection[str | Any | None]

with open(MAIN_TEXT_FILE, mode = 'r', encoding = 'utf-8') as file:
    rawLines = file.readlines()

for rawLine in rawLines:
    if isinstance(rawLine, str) and not rawLine.isspace():
        mainTextFileWords.add(rawLine.strip().lower())

mainTextFileWordsSize = len(mainTextFileWords)

with open(NEW_WORDS_TEXT_FILE, mode = 'r', encoding = 'utf-8') as file:
    rawLines = file.readlines()

for rawLine in rawLines:
    if isinstance(rawLine, str) and not rawLine.isspace():
        mainTextFileWords.add(rawLine.strip().lower())

newTextFileWordsSize = len(mainTextFileWords)
mainTextFileWordsList: list[str] = list(mainTextFileWords)
mainTextFileWordsList.sort(key = lambda word: word.casefold())

with open(MAIN_TEXT_FILE, mode = 'w', encoding = 'utf-8') as file:
    file.writelines(mainTextFileWordsList)

print(f'Original lines length was {mainTextFileWordsSize}, and the new lines length is {newTextFileWordsSize}')
