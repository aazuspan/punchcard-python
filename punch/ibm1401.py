"""Encoding information for IBM 1401 BCD."""

# Punched card size
ROWS = 12

# Zone and digit rows by index
ZONE_COLS = [None, 12, 11, 10]
DIGIT_COLS = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7]

# The order of rows on the punched card, from top to bottom
ROW_ORDER = [12, 11, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# IBM 1401 BCD hexadecimal encodings. I swapped a few unneeded characters for needed
# ones, but this still doesn't represent all Python operators.
# https://en.wikipedia.org/wiki/BCD_(character_encoding)
ENCODING = {
    " ": int("00", base=16),
    "1": int("01", base=16),
    "2": int("02", base=16),
    "3": int("03", base=16),
    "4": int("04", base=16),
    "5": int("05", base=16),
    "6": int("06", base=16),
    "7": int("07", base=16),
    "8": int("08", base=16),
    "9": int("09", base=16),
    "0": int("0A", base=16),
    "#": int("0B", base=16),
    "@": int("0C", base=16),
    ":": int("0D", base=16),
    ">": int("0E", base=16),
    "_": int("0F", base=16),  # Swapped for sqrt
    "/": int("11", base=16),
    "S": int("12", base=16),
    "T": int("13", base=16),
    "U": int("14", base=16),
    "V": int("15", base=16),
    "W": int("16", base=16),
    "X": int("17", base=16),
    "Y": int("18", base=16),
    "Z": int("19", base=16),
    "[": int("1A", base=16),  # Swapped for not-equal
    ",": int("1B", base=16),
    "%": int("1C", base=16),
    "=": int("1D", base=16),
    "'": int("1E", base=16),
    '"': int("1F", base=16),
    "-": int("20", base=16),
    "J": int("21", base=16),
    "K": int("22", base=16),
    "L": int("23", base=16),
    "M": int("24", base=16),
    "N": int("25", base=16),
    "O": int("26", base=16),
    "P": int("27", base=16),
    "Q": int("28", base=16),
    "R": int("29", base=16),
    "!": int("2A", base=16),
    "$": int("2B", base=16),
    "*": int("2C", base=16),
    ")": int("2D", base=16),
    ";": int("2E", base=16),
    "]": int("2F", base=16),  # Swapped for triangle
    "&": int("30", base=16),
    "A": int("31", base=16),
    "B": int("32", base=16),
    "C": int("33", base=16),
    "D": int("34", base=16),
    "E": int("35", base=16),
    "F": int("36", base=16),
    "G": int("37", base=16),
    "H": int("38", base=16),
    "I": int("39", base=16),
    "?": int("3A", base=16),
    ".": int("3B", base=16),
    "{": int("3C", base=16),  # Swapped for weird square
    "(": int("3D", base=16),
    "<": int("3E", base=16),
    "}": int("3F", base=16),  # Swapped for box
}
