"""Encode strings to punched cards."""

from .ibm1401 import ENCODING, ZONE_COLS, DIGIT_COLS

Column = list[int]
Card = list[Column]
Program = list[Card]


def _encode_char(char: str) -> Column:
    """Encode a character into a list of row numbers to punch."""
    char = str(char).upper()

    try:
        hex_encoding = ENCODING[char]
    except KeyError:
        raise ValueError(f"Unsupported character: {char}") from None

    # Convert the hexadecimal encoding to 6 bits. The two LMB encode the zone rows to
    # punch, while the remaining bits encode the digit row to punch.
    bin_encoding = bin(hex_encoding)[2:].zfill(6)
    zone = int(bin_encoding[:2], base=2)
    digit = int(bin_encoding[2:], base=2)

    # Include the zone and digit rows, plus row 8 for most special characters
    punched = [ZONE_COLS[zone], DIGIT_COLS[digit]] + ([8] if digit > 9 else [])

    return tuple(filter(lambda x: x is not None, punched))


def _encode_line(line: str, columns: int) -> Card:
    """Encode a line of text into a punched card."""
    if len(line) > columns:
        raise ValueError(f"Lines must be <= {columns} characters.")

    pad_columns = [[]] * (columns - len(line))
    return [_encode_char(char) for char in line] + pad_columns


def encode_source(prog: str, columns: int = 80) -> Program:
    """Encode a program into a list of punched cards."""
    # Skip whitespace lines
    lines = filter(lambda x: bool(x.strip()), prog.splitlines())
    return [_encode_line(line, columns=columns) for line in lines]
