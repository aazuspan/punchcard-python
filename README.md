# Punched Card Python

Encode Python[^sortof] onto [IBM 1401](https://en.wikipedia.org/wiki/IBM_1401) punched cards.

```
Row     Card 1 of 1
--------------------
12      ⬜️⬜️⬜️⬜️🔳️⬜️🔳️🔳️⬜️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️⬜️🔳️⬜️⬜️⬜️🔳️⬜️⬜️
11      🔳️🔳️⬜️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️
10      ⬜️⬜️🔳️⬜️⬜️🔳️⬜️⬜️🔳️⬜️⬜️🔳️🔳️🔳️⬜️🔳️⬜️🔳️⬜️⬜️⬜️🔳️🔳️⬜️🔳️🔳️🔳️⬜️⬜️⬜️
1       ⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
2       ⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️⬜️⬜️⬜️⬜️⬜️
3       ⬜️⬜️⬜️⬜️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️⬜️⬜️🔳️🔳️🔳️⬜️⬜️⬜️
4       ⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️🔳️⬜️⬜️⬜️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
5       ⬜️⬜️⬜️🔳️⬜️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️
6       ⬜️⬜️⬜️⬜️⬜️⬜️🔳️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️⬜️
7       🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
8       ⬜️⬜️⬜️⬜️⬜️🔳️🔳️⬜️🔳️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️⬜️🔳️🔳️🔳️🔳️🔳️⬜️
9       ⬜️🔳️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️⬜️🔳️⬜️⬜️⬜️⬜️⬜️⬜️🔳️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
```

## Requirements

- Python 3
- IBM 1401 mainframe, circa 1959[^caveat]

## Usage

Encode a Python string:

```bash
python -m punch --source "print('Hello, world!')" --columns=72
```

Or a Python file:

```bash
python -m punch --file test.py
```

## How?

A 12-row, 80 column IBM punched card can encode *most* ASCII characters[^sortof] that you'd need for a Python program[^python]. By encoding each character with the [IBM 1401 BCD encoding table](https://en.wikipedia.org/wiki/BCD_(character_encoding)#IBM_1401_BCD_code), we can generate one punched card for every line of Python code, creating a deck of punched cards to efficiently store our scripts.

More details in the [blog post](https://www.aazuspan.dev/blog/python_punchcards).

## Why?

Yeah, fair enough.

[^sortof]: Unless you need unicode, several operators including `+`, or any lowercase letters.
[^caveat]: That can run Python 3.
[^python]: Or any other language, really.
