import os
import sys


BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    text_length = len(text)
    flag_end = False
    punctuation_symbol = '.,!?:;'
    symbol_number = start + size - 1
    for symbol_end in range(start, text_length):
        if symbol_number == symbol_end:
            break
    else:
        flag_end = True

    if flag_end:
        return (text[start : symbol_end + 1], symbol_end - start + 1)
    if text[symbol_end] in punctuation_symbol and text[symbol_end + 1] not in punctuation_symbol:
        return (text[start : symbol_end + 1], symbol_end - start + 1)
    while text[symbol_end] not in punctuation_symbol or text[symbol_end + 1] in punctuation_symbol:
        symbol_end -= 1
    return (text[start : symbol_end + 1], symbol_end - start + 1)


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        book_file = file.read()
    start = 0
    page_count = 1
    text_length = len(book_file)
    while text_length:
        page_text, symbol_amount = _get_part_text(book_file, start, PAGE_SIZE)
        book[page_count] = page_text.lstrip()
        start = symbol_amount + start
        page_count += 1
        text_length -= symbol_amount


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
